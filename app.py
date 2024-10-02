from flask import Flask, render_template, request, redirect, session, url_for
from backend import database, google_books_api
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Für Session-Management

# Erstellt die Tabellen, falls sie nicht existieren
with app.app_context():
    database.create_tables()

@app.route('/')
def index():
    """
    Zeigt die Startseite an.
    """
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Diese Route verarbeitet die Registrierung eines neuen Benutzers.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Benutzer registrieren
        database.register_user(username, password)
        
        # Leitet den Benutzer zur Login-Seite weiter
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Diese Route verarbeitet den Login eines Benutzers.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Überprüfen, ob der Benutzer existiert
        user = database.authenticate_user(username, password)
        if user:
            # Greife auf die Benutzer-ID über das erste Element des Tuples zu
            session['user_id'] = user[0]  # user[0] ist die ID des Benutzers
            return redirect('/search')
        else:
            return 'Login fehlgeschlagen. Bitte überprüfe deinen Benutzernamen und dein Passwort.'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Diese Route verarbeitet das Ausloggen des Benutzers.
    """
    session.pop('user_id', None)
    return redirect('/')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Diese Route zeigt das Suchformular und verarbeitet die Suchanfrage des Benutzers.
    """
    if 'user_id' not in session:
        return redirect('/login')  # Benutzer muss eingeloggt sein
    
    if request.method == 'POST':
        field_of_interest = request.form['field']
        specific_topic = request.form.get('topic', '')
        
        # Bücher von der Google Books API basierend auf den Suchkriterien abrufen
        books = google_books_api.search_books(field_of_interest, specific_topic)
        
        # Ergebnisse anzeigen
        return render_template('results.html', books=books)
    
    return render_template('search.html')

@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    """
    Diese Route zeigt und speichert die Favoriten des Benutzers.
    """
    if 'user_id' not in session:
        return redirect('/login')  # Benutzer muss eingeloggt sein
    
    user_id = session['user_id']
    
    if request.method == 'POST':
        # Vom Benutzer ausgewählte Bücher abrufen
        selected_books = request.form.getlist('selected_books')
        
        # Jedes ausgewählte Buch in die Favoriten speichern
        for isbn in selected_books:
            book = google_books_api.get_book_by_isbn(isbn)
            
            if book is None:
                # Wenn kein Buch gefunden wurde, gib eine entsprechende Meldung aus oder ignoriere es
                return 'Kein Buch mit der ISBN gefunden.'
            
            # Buch zu den Favoriten hinzufügen
            database.save_favorite(user_id, book)
        
        return redirect('/favorites')
    
    # Favoriten des Benutzers anzeigen
    favorites = database.get_favorites(user_id)
    return render_template('favorites.html', favorites=favorites)

@app.route('/remove_favorites', methods=['POST'])
def remove_favorites_view():
    """
    Diese Route verarbeitet das Entfernen der ausgewählten Favoriten des Benutzers.
    """
    if 'user_id' in session:
        selected_isbns = request.form.getlist('selected_books')
        if selected_isbns:
            # Entferne die ausgewählten Favoriten
            database.remove_favorites(session['user_id'], selected_isbns)
        return redirect(url_for('favorites'))  # Leitet zur Favoritenliste zurück
    return redirect(url_for('login'))



#Ignore