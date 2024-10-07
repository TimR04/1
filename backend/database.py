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
logging.basicConfig(filename='application.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


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
    Creates the 'users' and 'reading_progress' tables in the database if they do not exist.
    The 'users' table stores user information, and the 'reading_progress' table stores 
    the user's reading progress with foreign keys linking to the 'users' and 'books' tables.
    
    Returns:
        None

    Tests:
        1. **Table Creation Success**:
            - Input: Call create_tables() when the database is empty.
            - Expected Outcome: Tables 'users' and 'reading_progress' are created successfully without raising any errors.
        
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
    Registriert einen neuen Benutzer, speichert den gehashten Benutzernamen und das gehashte Passwort.
    """
    hashed_username = hash_username(username)
    hashed_password = hash_password(password)
    
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (hashed_username, hashed_password))
        conn.commit()
        logging.info(f"Benutzer '{username}' erfolgreich registriert.")
    except sqlite3.Error as e:
        logging.error(f"Error during user registration: {e}")
    finally:
        conn.close()


def authenticate_user(username, password):
    """
    Authentifiziert den Benutzer durch Überprüfung des gehashten Benutzernamens und des Passworts.
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
        stored_username_hash = user[1]  # Der gehashte Benutzername aus der DB
        if check_username_hash(stored_username_hash, username):
            if check_password(user[2], password):
                logging.info(f"User '{username}' successfully authenticated.")
                return user
    logging.warning(f"Authentication failed for user '{username}'.")
    return None



def hash_password(password):
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(hashed_password, password):
    """Verifies a password against the hashed version."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def hash_username(username):
    """Hash the username using SHA-256."""
    return hashlib.sha256(username.encode('utf-8')).hexdigest()


def check_username_hash(stored_hash, username):
    """Checks if the SHA-256 hash of the username matches the stored hash."""
    return stored_hash == hash_username(username)

