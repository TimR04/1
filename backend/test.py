import sqlite3

def show_all_data():
    conn = sqlite3.connect('database.db')  # Ersetze 'database.db' mit deinem Datenbanknamen
    cur = conn.cursor()

    # Beispielabfrage, um alle Benutzer anzuzeigen
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

import os

def delete_database(db_name='database.db'):
    """
    Deletes the SQLite database file if it exists.

    Args:
        db_name (str): The name of the database file to delete.
    """
    try:
        if os.path.exists(db_name):
            os.remove(db_name)
            print(f"Database '{db_name}' deleted successfully.")
        else:
            print(f"Database '{db_name}' does not exist.")
    except Exception as e:
        print(f"Error deleting the database: {e}")


if __name__ == "__main__":
    show_all_data()
