import json
import os

# Path to the JSON file for favorites
FAVORITES_JSON_PATH = 'favorites.json'


def load_all_favorites():
    """Load all favorites from the JSON file."""
    if not os.path.exists(FAVORITES_JSON_PATH):
        return {}

    try:
        with open(FAVORITES_JSON_PATH, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}



def load_user_favorites(user_id):
    """Load favorites for a specific user."""
    all_favorites = load_all_favorites()
    return all_favorites.get(str(user_id), [])


def save_favorite(user_id, book_details):
    """Save a favorite book for a user in the JSON file."""
    all_favorites = load_all_favorites()

    if str(user_id) not in all_favorites:
        all_favorites[str(user_id)] = []

    # Check if the book already exists
    existing_book = next((book for book in all_favorites[str(user_id)] if book['isbn'] == book_details['isbn']), None)

    if not existing_book:
        all_favorites[str(user_id)].append(book_details)

        # Write the updated favorites back to the JSON file
        with open(FAVORITES_JSON_PATH, 'w') as file:
            json.dump(all_favorites, file, indent=4)


def save_favorite_learning(user_id, book_isbn, learning):
    """Save a learning note for a book in the favorites JSON file."""
    all_favorites = load_all_favorites()

    if str(user_id) in all_favorites:
        # Find the book by its ISBN and update its learning note
        for book in all_favorites[str(user_id)]:
            if book['isbn'] == book_isbn:
                book['learning'] = learning
                break

        # Write the updated favorites back to the JSON file
        with open(FAVORITES_JSON_PATH, 'w') as file:
            json.dump(all_favorites, file, indent=4)


def remove_favorites(user_id, selected_isbns):
    """Remove selected favorites for a user from the JSON file."""
    all_favorites = load_all_favorites()

    if str(user_id) in all_favorites:
        # Filter out the books whose ISBN is in the selected_isbns list
        all_favorites[str(user_id)] = [
            book for book in all_favorites[str(user_id)] if book['isbn'] not in selected_isbns
        ]

        # Write the updated favorites back to the JSON file
        with open(FAVORITES_JSON_PATH, 'w') as file:
            json.dump(all_favorites, file, indent=4)


def update_favorite_page(user_id, book_isbn, current_page):
    """Update the current page number of a favorite book for the user."""
    all_favorites = load_all_favorites()

    if str(user_id) in all_favorites:
        # Find the book by its ISBN and update the current page number
        for book in all_favorites[str(user_id)]:
            if book['isbn'] == book_isbn:
                book['current_page'] = current_page
                break

        # Write the updated favorites back to the JSON file
        with open(FAVORITES_JSON_PATH, 'w') as file:
            json.dump(all_favorites, file, indent=4)
