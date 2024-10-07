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
from datetime import datetime, timedelta

# Set up logging configuration
logging.basicConfig(
    filename='application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def connect_to_db():
    """
    Establishes a connection to the SQLite database.

    Returns:
        Connection object: SQLite connection to 'database.db'.
    """
    try:
        conn = sqlite3.connect('database.db')
        logging.info("Database connection established successfully.")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        raise e

# User Management Functions

def create_user_table():
    """
    Creates the 'users' table in the database if it does not exist.

    Returns:
        None

    Tests:
        1. **Table Creation Success**:
            - Input: Call create_user_table() when the database is empty.
            - Expected Outcome: Tables 'users' are created successfully without raising any errors.
        
        2. **Table Existence Check**:
            - Input: Call create_user_table() twice in a row.
            - Expected Outcome: The second call should not raise any errors, and the tables should remain unchanged.
    """
    conn = connect_to_db()
    cur = conn.cursor()
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                last_read_date DATE,
                current_streak INTEGER DEFAULT 0,
                longest_streak INTEGER DEFAULT 0
            )
        ''')
        logging.info("Table 'users' created or already exists.")
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error creating 'users' table: {e}")
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
        conn = connect_to_db()
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
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT id, username, password FROM users")
        users = cur.fetchall()
    except sqlite3.Error as e:
        logging.error(f"Error during authentication: {e}")
        return None
    finally:
        conn.close()

    for user in users:
        stored_username_hash = user[1]
        if check_username_hash(stored_username_hash, username):
            if check_password(user[2], password):
                logging.info(f"User '{username}' successfully authenticated.")
                return user
    logging.warning(f"Authentication failed for user '{username}'.")
    return None

# Password and Username Hashing Functions

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
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def hash_username(username):
    """
    Hashes the username using SHA-256.

    Args:
        username (str): The username to be hashed.

    Returns:
        str: The SHA-256 hash of the username.
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
    """
    return stored_hash == hash_username(username)

# Reading Streak Management Functions

def update_reading_streak(user_id):
    """
    Updates the user's reading streak based on their last reading date.
    
    Args:
        user_id (int): The ID of the user.
    
    Returns:
        dict: A dictionary containing the user's updated current streak, longest streak, last read date, and streak status.
    """
    conn = connect_to_db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT last_read_date, current_streak, longest_streak FROM users WHERE id = ?", (user_id,))
        user_data = cur.fetchone()

        last_read_date_str, current_streak, longest_streak = user_data if user_data else (None, 0, 0)
        last_read_date = datetime.strptime(last_read_date_str, '%Y-%m-%d').date() if last_read_date_str else None

        today = datetime.now().date()

        if last_read_date == today:
            streak_status = "unchanged"
        elif last_read_date == today - timedelta(days=1):
            current_streak += 1
            streak_status = "continued"
        else:
            current_streak = 1
            streak_status = "reset"

        if current_streak > longest_streak:
            longest_streak = current_streak

        cur.execute(
            "UPDATE users SET last_read_date = ?, current_streak = ?, longest_streak = ? WHERE id = ?",
            (today.strftime('%Y-%m-%d'), current_streak, longest_streak, user_id)
        )
        conn.commit()

        logging.info(f"User {user_id} streak updated: Current streak is {current_streak}, Longest streak is {longest_streak}, Status: {streak_status}.")
        return {
            "current_streak": current_streak,
            "longest_streak": longest_streak,
            "last_read_date": today,
            "streak_status": streak_status
        }

    except sqlite3.Error as e:
        logging.error(f"Database error while updating reading streak for user {user_id}: {e}")
        return {
            "current_streak": 0,
            "longest_streak": 0,
            "last_read_date": None,
            "streak_status": "error"
        }
    finally:
        conn.close()

def get_user_streak_data(user_id):
    """
    Retrieves the user's streak data from the database.
    
    Args:
        user_id (int): The ID of the user.
    
    Returns:
        dict: A dictionary containing 'current_streak', 'longest_streak', and 'last_read_date'.
    """
    conn = connect_to_db()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT current_streak, longest_streak, last_read_date FROM users WHERE id = ?", (user_id,))
        result = cur.fetchone()
        
        if result:
            current_streak, longest_streak, last_read_date = result
            return {
                "current_streak": current_streak,
                "longest_streak": longest_streak,
                "last_read_date": last_read_date
            }
        return {
            "current_streak": 0,
            "longest_streak": 0,
            "last_read_date": None
        }
    except sqlite3.Error as e:
        logging.error(f"Error retrieving streak data for user {user_id}: {e}")
        return {
            "current_streak": 0,
            "longest_streak": 0,
            "last_read_date": None
        }
    finally:
        conn.close()
