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

if __name__ == "__main__":
    show_all_data()
