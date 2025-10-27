import random
import pytest

from main import BooksCollector


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    for i in range(8):
        collector.add_new_book(f'Книга {i}')
    return collector


@pytest.fixture
def collector_with_genres(collector_with_books):
    for book in collector_with_books.books_genre.keys():
        genre = random.choice(collector_with_books.genre)
        collector_with_books.set_book_genre(book, genre)
    return collector_with_books


@pytest.fixture
def collector_with_favorites(collector_with_books):
    for book in collector_with_books.books_genre.keys():
        collector_with_books.add_book_in_favorites(book)
    return collector_with_books
