import sqlite3

def connect_db():
    """Verbindung zur SQLite-Datenbank herstellen."""
    return sqlite3.connect('database.db')

def create_tables():
    """
    Diese Funktion erstellt die Tabellen für Benutzer (users) 
    und Favoriten (favorites), falls sie noch nicht existieren.
    Außerdem wird die Spalte 'category' zu 'favorites' hinzugefügt, falls sie nicht existiert.
    """
    conn = connect_db()
    cur = conn.cursor()

    # Erstellen der Tabelle 'users', falls sie nicht existiert
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')


    cur.execute('''
        CREATE TABLE IF NOT EXISTS reading_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            book_title TEXT,
            date DATE DEFAULT (DATE('now')),
            pages_read INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    ''')

    conn.commit()
    conn.close()


def register_user(username, password):
    """
    Diese Funktion speichert einen neuen Benutzer in der Datenbank.
    """
    conn = connect_db()
    cur = conn.cursor()
    
    # Benutzerinformationen in die Tabelle 'users' einfügen
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    """
    Diese Funktion überprüft die Anmeldedaten eines Benutzers.
    Gibt den Benutzer als Tuple zurück (id, username, password).
    """
    conn = connect_db()
    cur = conn.cursor()
    
    # Benutzerinformationen abrufen
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()  # Gibt ein Tuple zurück: (id, username, password)
    
    conn.close()
    
    return user  # Gibt das Tuple zurück oder None, wenn der Benutzer nicht existiert



