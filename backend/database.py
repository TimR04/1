"""
Database Module

- This module handles the SQLite database connection and operations such as user registration, authentication, and table creation for a book recommendation application.

Author: Paul, Tim, Thang
Date: 06.10.2024
Version: 0.1.0
License: Free
"""

import sqlite3
import logging
import bcrypt
import hashlib

# Set up logging configuration
logging.basicConfig(
    filename='application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def connect_db():
    """
    Establishes a connection to the SQLite database.

    Returns:
        Connection object: SQLite connection to 'database.db'.

    Tests:
        1. **Database Connection Success**:
            - Input: Attempt to connect to the database.
            - Expected Outcome: A connection object is returned if the database exists.
        
        2. **Database Connection Error Handling**:
            - Input: (Simulate) Attempt to connect to a non-existent database.
            - Expected Outcome: An exception should be raised indicating that the database cannot be found (this requires a mock or testing environment).
    """
    try:
        conn = sqlite3.connect('database.db')
        logging.info("Database connection established successfully.")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        raise e


def create_tables():
    """
    Creates the 'users' table in the database if it does not exist.

    Returns:
        None

    Tests:
        1. **Table Creation Success**:
            - Input: Call create_tables() when the database is empty.
            - Expected Outcome: Tables 'users' are created successfully without raising any errors.
        
        2. **Table Existence Check**:
            - Input: Call create_tables() twice in a row.
            - Expected Outcome: The second call should not raise any errors, and the tables should remain unchanged.
    """
    conn = connect_db()
    cur = conn.cursor()

    try:
        # Create 'users' table if it does not exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        logging.info("Table 'users' created or already exists.")
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")
        raise e
    finally:
        conn.close()


def register_user(username, password):
    """
    Registers a new user by storing the hashed username and password.

    Args:
        username (str): The user's username.
        password (str): The user's password.

    Tests:
        1. **Successful Registration**:
            - Input: Valid username and password.
            - Expected Outcome: User is added to the database, and no errors occur.
        
        2. **Duplicate Registration Handling**:
            - Input: Register a user with a username that already exists.
            - Expected Outcome: An appropriate error message is logged, and no duplicate entries are created.
    """
    hashed_username = hash_username(username)
    hashed_password = hash_password(password)

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (hashed_username, hashed_password)
        )
        conn.commit()
        logging.info(f"User '{username}' successfully registered.")
    except sqlite3.Error as e:
        logging.error(f"Error during user registration: {e}")
    finally:
        conn.close()


def authenticate_user(username, password):
    """
    Authenticates the user by checking the hashed username and password.

    Args:
        username (str): The user's username.
        password (str): The user's password.

    Returns:
        tuple or None: Returns the user tuple if authentication is successful, otherwise None.

    Tests:
        1. **Successful Authentication**:
            - Input: Correct username and password.
            - Expected Outcome: Returns user information if credentials match.
        
        2. **Failed Authentication**:
            - Input: Incorrect username or password.
            - Expected Outcome: Returns None and logs a warning message.
    """
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password FROM users")
        users = cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error during authentication: {e}")
        return None
    finally:
        conn.close()

    for user in users:
        stored_username_hash = user[1]  # The hashed username from the DB
        if check_username_hash(stored_username_hash, username):
            if check_password(user[2], password):
                logging.info(f"User '{username}' successfully authenticated.")
                return user
    logging.warning(f"Authentication failed for user '{username}'.")
    return None


def hash_password(password):
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.

    Tests:
        1. **Hash Generation**:
            - Input: A sample password.
            - Expected Outcome: Returns a bcrypt hash string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_password(hashed_password, password):
    """
    Verifies a password against the hashed version.

    Args:
        hashed_password (str): The hashed password from the database.
        password (str): The plain text password to verify.

    Returns:
        bool: True if the password matches, False otherwise.

    Tests:
        1. **Correct Password**:
            - Input: A correct plain text password and its hash.
            - Expected Outcome: Returns True.
        
        2. **Incorrect Password**:
            - Input: A wrong plain text password and a hash.
            - Expected Outcome: Returns False.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def hash_username(username):
    """
    Hashes the username using SHA-256.

    Args:
        username (str): The username to be hashed.

    Returns:
        str: The SHA-256 hash of the username.

    Tests:
        1. **Hash Generation**:
            - Input: A sample username.
            - Expected Outcome: Returns a SHA-256 hash string.
    """
    return hashlib.sha256(username.encode('utf-8')).hexdigest()


def check_username_hash(stored_hash, username):
    """
    Checks if the SHA-256 hash of the username matches the stored hash.

    Args:
        stored_hash (str): The stored hash value from the database.
        username (str): The plain text username to verify.

    Returns:
        bool: True if the hash matches, False otherwise.

    Tests:
        1. **Correct Username Match**:
            - Input: A correct username and its stored hash.
            - Expected Outcome: Returns True.
        
        2. **Incorrect Username Match**:
            - Input: A wrong username and a stored hash.
            - Expected Outcome: Returns False.
    """
    return stored_hash == hash_username(username)
