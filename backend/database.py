import sqlite3

def connect_db():
    """Verbindung zur SQLite-Datenbank herstellen."""
    return sqlite3.connect('database.db')

def create_tables():
    """
    Diese Funktion erstellt die Tabellen für Benutzer (users) 
    und Favoriten (favorites), falls sie noch nicht existieren.
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
    
    # Erstellen der Tabelle 'favorites', falls sie nicht existiert
    cur.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_title TEXT,
            author TEXT,
            isbn TEXT,
            publication_year TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Änderungen speichern und Verbindung schließen
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

def save_favorite(user_id, book_details):
    """
    Diese Funktion speichert ein Buch als Favorit für den Benutzer.
    """
    conn = connect_db()
    cur = conn.cursor()
    
    # Buchinformationen in die Tabelle 'favorites' einfügen
    cur.execute('''INSERT INTO favorites (user_id, book_title, author, isbn, publication_year)
                   VALUES (?, ?, ?, ?, ?)''',
                (user_id, book_details['title'], book_details['author'],
                 book_details['isbn'], book_details['publication_year']))
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

def get_favorites(user_id):
    """
    Diese Funktion ruft die Favoriten eines Benutzers ab und gibt eine Liste von Büchern zurück.
    """
    conn = connect_db()
    cur = conn.cursor()
    
    # Favoriten für den Benutzer abrufen
    cur.execute("SELECT book_title, author, isbn, publication_year FROM favorites WHERE user_id = ?", (user_id,))
    favorites = cur.fetchall()
    
    conn.close()
    
    # Favoriten in ein lesbares Format umwandeln
    return [{'title': row[0], 'author': row[1], 'isbn': row[2], 'publication_year': row[3]} for row in favorites]

def remove_favorites(user_id, selected_isbns):
    """
    Entfernt die ausgewählten Favoriten eines Benutzers aus der Datenbank.
    """
    conn = connect_db()
    cur = conn.cursor()
    
    # Entferne die Favoriten, deren ISBN in der Liste der ausgewählten ISBNs ist
    cur.execute('''
        DELETE FROM favorites 
        WHERE user_id = ? AND isbn IN ({seq})
    '''.format(seq=','.join(['?']*len(selected_isbns))), [user_id] + selected_isbns)
    
    conn.commit()
    conn.close()