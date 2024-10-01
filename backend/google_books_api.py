import requests

def search_books(field_of_interest, specific_topic):
    """Sucht Bücher basierend auf dem Fachgebiet und dem Thema."""
    query = f'{field_of_interest} {specific_topic}'
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(url)
    data = response.json()

    books = []
    for item in data.get('items', [])[:5]:  # Begrenzung auf 5 Bücher
        book_info = item.get('volumeInfo', {})

        # Füge die Buchbeschreibung hinzu
        books.append({
            'title': book_info.get('title', 'N/A'),
            'author': ', '.join(book_info.get('authors', ['N/A'])),
            'isbn': book_info.get('industryIdentifiers', [{'identifier': 'N/A'}])[0]['identifier'],
            'publication_year': book_info.get('publishedDate', 'N/A'),
            'description': book_info.get('description', 'Keine Beschreibung verfügbar')  # Neue Beschreibung hinzugefügt
        })

    return books


def get_book_by_isbn(isbn):
    """
    Diese Funktion ruft Buchdetails basierend auf der ISBN ab.
    Überprüft, ob die Antwort gültig ist und das Feld 'items' enthält.
    """
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    response = requests.get(url)
    data = response.json()

    # Überprüfen, ob 'items' im Antwort-JSON vorhanden ist
    if 'items' not in data:
        return None  # Keine Ergebnisse gefunden
    
    item = data['items'][0]
    book_info = item.get('volumeInfo', {})

    return {
        'title': book_info.get('title', 'N/A'),
        'author': ', '.join(book_info.get('authors', ['N/A'])),
        'isbn': book_info.get('industryIdentifiers', [{'identifier': 'N/A'}])[0]['identifier'],
        'publication_year': book_info.get('publishedDate', 'N/A'),
        'description': book_info.get('description', 'Keine Beschreibung verfügbar')  # Beschreibung hinzugefügt
    }