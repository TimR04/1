"""
Book Recommendation App

- This Flask application serves as a front-end for a book recommendation system. 
- Users can register, log in, search for books using the Google Books API, and save their favorites. 
- Favorites are stored in JSON format, and users can manage them through the app.

Author: Paul, Tim, Thang
Date: 06.10.2024
Version: 0.1.0 (major.minor.bugfix)
License: Free
"""

import os
from flask import Flask, render_template, request, redirect, session, url_for
from flask.cli import load_dotenv
from backend import database, google_books_api, json_storage
import logging

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Set up logging configuration
logging.basicConfig(filename='application.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')



@app.route('/')
def index():
    """
    Displays the homepage with streak information if the user is logged in.
    
    Returns:
        Rendered homepage (index.html).
    """
    user_id = session.get('user_id')

    # Initialize streak data as empty
    streak_data = None

    # If the user is logged in, get the streak data
    if user_id:
        streak_data = database.get_user_streak_data(user_id)
        logging.info(f"Displayed streak data for user {user_id}.")
    else:
        logging.info("Homepage accessed without login.")

    return render_template('index.html', streak_data=streak_data)




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Benutzer registrieren
        database.register_user(username, password)
        return redirect('/login')
    
    return render_template('register.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = database.authenticate_user(username, password)
        if user:
            session['user_id'] = user[0]  # Store user ID in session
            return redirect('/')
        else:
            return 'Login failed. Please check your username and password.'
    
    return render_template('login.html')





@app.route('/streaks')
def streaks():
    if 'user_id' not in session:
        logging.warning("User attempted to access streaks page without logging in.")
        return "Log in to track your reading streaks."
    
    # Rest of your code to display streaks
    return render_template('streaks.html', user_id=session['user_id'])



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    logging.info("User logged out.")
    return redirect('/')


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Displays the search form and processes the user's search query.
    
    POST:
        Retrieves books from the Google Books API based on user input (field and topic).

    Returns:
        Renders the search results page if successful or the search form for a GET request.
    """
    if 'user_id' not in session:
        logging.warning("Unauthorized access to search page.")
        return redirect('/login')  # User must be logged in

    if request.method == 'POST':
        field_of_interest = request.form['field']
        specific_topic = request.form.get('topic', '')

        # Retrieve books from the Google Books API based on search criteria
        books = google_books_api.search_books(field_of_interest, specific_topic)
        logging.info(f"Search query '{field_of_interest}' with topic '{specific_topic}' returned {len(books)} results.")
        return render_template('results.html', books=books, category=field_of_interest)

    return render_template('search.html')


@app.route('/favorites', methods=['GET'])
def favorites():
    """
    Displays the user's favorite books.
    
    Returns:
        Renders the favorites page with the user's favorite books filtered by category if applicable.
    """
    user_id = session.get('user_id')

    # Load all favorites and filter only the current user's favorites
    all_favorites = json_storage.load_all_favorites()
    favorites_json = all_favorites.get(str(user_id), [])

    # Optional: Filter by category
    category_filter = request.args.get('category', None)
    if category_filter:
        favorites_json = [book for book in favorites_json if book.get('category') == category_filter]

    logging.info(f"Favorites displayed for user {user_id} with category filter '{category_filter}'.")
    return render_template('favorites.html', favorites=favorites_json, category_filter=category_filter)


@app.route('/remove_favorites', methods=['POST'])
def remove_favorites_view():
    """
    Handles removing selected favorite books for a user.
    
    POST:
        Removes the books with the selected ISBNs from the user's favorites list.

    Returns:
        Redirects to the favorites page.
    """
    if 'user_id' in session:
        user_id = session['user_id']
        selected_isbns = request.form.getlist('selected_books')

        if selected_isbns:
            json_storage.remove_favorites(user_id, selected_isbns)
            logging.info(f"Removed favorites for user {user_id}: {selected_isbns}")

        return redirect(url_for('favorites'))
    logging.warning("Unauthorized attempt to remove favorites.")
    return redirect(url_for('login'))


@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    """
    Adds selected books to the user's favorites.
    
    POST:
        Saves the selected books (with title, author, ISBN, publication year) to the user's favorites list.

    Returns:
        Redirects to the favorites page.
    """
    user_id = session.get('user_id')

    selected_books = request.form.getlist('selected_books')
    if not selected_books:
        logging.error("No books selected to add to favorites.")
        return "No books selected.", 400

    for index in selected_books:
        title = request.form.get(f'title_{index}')
        author = request.form.get(f'author_{index}')
        isbn = request.form.get(f'isbn_{index}')
        publication_year = request.form.get(f'publication_year_{index}')
        category = request.form.get(f'category_{index}', 'Uncategorized')

        if not all([title, author, isbn, publication_year]):
            logging.error("Missing data for one of the books.")
            return "Missing data for one of the books.", 400

        # Prepare book details
        book_details = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'publication_year': publication_year,
            'category': category
        }

        json_storage.save_favorite(user_id, book_details)
        logging.info(f"Added favorite book '{title}' for user {user_id}.")

    return redirect('/favorites')


@app.route('/test_json_favorites', methods=['GET'])
def test_json_favorites():
    """
    Test route to display the contents of the favorites JSON file.
    
    Returns:
        Renders a template displaying the contents of the JSON file.
    """
    favorites_data = json_storage.load_all_favorites()
    logging.info("Displayed test JSON favorites data.")
    return render_template('test_json.html', favorites_data=favorites_data)


@app.route('/bookmark', methods=['GET'])
def bookmark():
    """
    Displays the user's bookmarks.
    
    Returns:
        Renders the bookmarks page with the user's bookmarked books.
    """
    user_id = session.get('user_id')
    if not user_id:
        logging.warning("Unauthorized access to bookmarks.")
        return redirect('/login')

    # Load all favorites and filter for the current user
    all_favorites = json_storage.load_all_favorites()
    favorites = all_favorites.get(str(user_id), [])

    logging.info(f"Displayed bookmarks for user {user_id}.")
    return render_template('bookmarks.html', favorites=favorites)


@app.route('/update_favorite_page', methods=['POST'])
def update_favorite_page():
    """
    Updates the current page for a favorite book and the user's reading streak.
    """
    user_id = session.get('user_id')
    if not user_id:
        logging.warning("Unauthorized attempt to update favorite page.")
        return redirect('/login')  # User must be logged in

    # Get data from the form
    book_isbn = request.form['book_isbn']
    current_page = request.form['current_page']

    try:
        current_page = int(current_page)  # Ensure page number is a valid integer
    except ValueError:
        logging.error(f"Invalid page number '{current_page}' provided.")
        return "Invalid page number", 400

    # Update the current page in the JSON file
    json_storage.update_favorite_page(user_id, book_isbn, current_page)
    logging.info(f"Updated page to {current_page} for book with ISBN {book_isbn} for user {user_id}.")

    # Update the user's reading streak
    database.update_reading_streak(user_id)

    # Reload the page with the updated data
    favorites = json_storage.load_user_favorites(user_id)
    return render_template('bookmarks.html', favorites=favorites)


@app.route('/learnings', methods=['GET', 'POST'])
def learnings():
    """
    Displays and saves learning notes for a user's favorite books.
    
    POST:
        Saves learning notes for a book in the user's favorites.

    Returns:
        Renders the learning notes page.
    """
    user_id = session.get('user_id')
    if not user_id:
        logging.warning("Unauthorized access to learnings.")
        return redirect('/login')

    if request.method == 'POST':
        book_isbn = request.form['book_isbn']
        learning = request.form['learning']

        json_storage.save_favorite_learning(user_id, book_isbn, learning)
        logging.info(f"Saved learning for book with ISBN {book_isbn} for user {user_id}.")

        return redirect('/learnings')

    favorites = json_storage.load_user_favorites(user_id)
    return render_template('learnings.html', favorites=favorites)

@app.route('/update_reading_progress', methods=['POST'])
def update_reading_progress():
    """
    Updates the user's reading progress and their streak.
    """
    user_id = session.get('user_id')
    if user_id:
        current_page = request.form.get('current_page')
        # Update the reading streak based on the progress
        streak_data = database.update_reading_streak(user_id)
        return redirect('/')
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
