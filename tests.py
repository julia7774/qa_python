import random
import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        "name, result",
        [
            ['Книга', 1],
            ['Книга' * 40, 0],
        ]
    )
    def test_add_new_book(self, name, result):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == result

    def test_add_new_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_length(self):
        collector = BooksCollector()

        collector.add_new_book('К' * 42)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, collector_with_books):
        for book in collector_with_books.books_genre.keys():
            assert collector_with_books.get_book_genre(book) == ''
            genre = random.choice(collector_with_books.genre)

            collector_with_books.set_book_genre(book, genre)
            assert collector_with_books.get_book_genre(book) == genre

    def test_set_book_genre_invalid_genre(self, collector_with_books):
        genre = 'Жанр'
        for book in collector_with_books.books_genre.keys():
            assert collector_with_books.get_book_genre(book) == ''

            collector_with_books.set_book_genre(book, genre)
            assert collector_with_books.get_book_genre(book) == ''

    def test_get_book_genre(self, collector_with_genres):
        for book, genre in collector_with_genres.books_genre.items():
            assert collector_with_genres.get_book_genre(book) == genre

    def test_get_book_genre_invalid_book(self):
        collector = BooksCollector()
        assert not collector.get_book_genre('Книга')

    def test_get_books_with_specific_genre(self, collector_with_genres):
        for genre in collector_with_genres.genre:
            books = collector_with_genres.get_books_with_specific_genre(genre)

            assert all(collector_with_genres.books_genre[book] == genre for book in books)
            books_with_genre = 0
            for value in collector_with_genres.books_genre.values():
                if value == genre:
                    books_with_genre += 1

            assert len(books) == books_with_genre

    def test_get_books_genre(self, collector_with_genres):
        result = collector_with_genres.get_books_genre()

        assert result == collector_with_genres.books_genre
        assert len(result) == len(collector_with_genres.books_genre)

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert not collector.get_books_genre()

    def test_get_books_for_children(self, collector_with_genres):
        books = collector_with_genres.get_books_for_children()

        for name, genre in collector_with_genres.books_genre.items():
            if genre in collector_with_genres.genre_age_rating:
                assert name not in books
            else:
                assert name in books

    def test_get_books_for_children_empty(self):
        collector = BooksCollector()
        assert not collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector_with_genres):
        assert not collector_with_genres.get_list_of_favorites_books()

        for name in collector_with_genres.books_genre.keys():
            collector_with_genres.add_book_in_favorites(name)
            assert name in collector_with_genres.favorites

    def test_delete_book_from_favorites(self, collector_with_favorites):
        for name in collector_with_favorites.books_genre.keys():
            collector_with_favorites.delete_book_from_favorites(name)
            assert name not in collector_with_favorites.favorites

    def test_get_list_of_favorites_books(self, collector_with_favorites):
        favorites = collector_with_favorites.get_list_of_favorites_books()
        assert len(favorites) == len(collector_with_favorites.favorites)

    def test_get_list_of_favorites_books_empty(self, collector_with_genres):
        favorites = collector_with_genres.get_list_of_favorites_books()
        assert len(favorites) == len(collector_with_genres.favorites)
        assert len(favorites) == 0
