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
        "name, expected",
        [
            ['Книга', 1],
            ['Книга' * 40, 0],
        ]
    )
    def test_add_new_book(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected

    def test_add_new_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_length(self):
        collector = BooksCollector()

        collector.add_new_book('К' * 42)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        "book, genre",
        [
            ['Книга', 'Фантастика'],
            ['Книга', 'Детективы'],
        ]
    )
    def test_set_book_genre(self, collector, book, genre):
        collector.add_new_book(book)
        assert collector.books_genre[book] == ''
        collector.set_book_genre(book, genre)
        assert collector.books_genre[book] == genre

    def test_set_book_genre_invalid_genre(self, collector):
        book = 'Книга'
        collector.add_new_book(book)
        genre = 'Жанр'
        assert collector.books_genre[book] == ''
        collector.set_book_genre(book, genre)
        assert collector.books_genre[book] == ''

    @pytest.mark.parametrize(
        "book, genre",
        [
            ['Книга', 'Фантастика'],
            ['Книга', 'Детективы'],
        ]
    )
    def test_get_book_genre(self, collector, book, genre):
        collector.books_genre = {book: genre}
        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_invalid_book(self, collector):
        assert not collector.get_book_genre('Книга')

    def test_get_books_with_specific_genre(self, collector):
        genre_count = {}
        for i in range(8):
            book = f'Книга {i}'
            collector.add_new_book(book)
            genre = random.choice(collector.genre)
            collector.set_book_genre(book, genre)
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

        for genre in collector.genre:
            books = collector.get_books_with_specific_genre(genre)

            assert all(collector.books_genre[book] == genre for book in books)
            books_with_genre = 0
            assert len(books) == genre_count.get(genre, 0)

    def test_get_books_genre(self, collector):
        for i in range(8):
            book = f'Книга {i}'
            collector.add_new_book(book)

        result = collector.get_books_genre()

        assert result == collector.books_genre
        assert len(result) == len(collector.books_genre)

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert not collector.get_books_genre()

    @pytest.mark.parametrize(
        "book, genre, expected",
        [
            ['Книга', 'Ужасы', []],
            ['Книга', 'Мультфильмы', ['Книга']],
        ]
    )
    def test_get_books_for_children(self, collector, book, genre, expected):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        books = collector.get_books_for_children()
        assert books == expected

    def test_get_books_for_children_empty(self, collector):
        assert not collector.get_books_for_children()


    def test_add_book_in_favorites(self, collector):
        book = 'Книга'
        collector.add_new_book(book)
        assert len(collector.favorites) == 0
        collector.add_book_in_favorites(book)
        assert book in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        book = 'Книга'
        collector.add_new_book(book)
        collector.favorites = [book]
        assert book in collector.favorites
        collector.delete_book_from_favorites(book)
        assert book not in collector.favorites


    @pytest.mark.parametrize(
        "book, favorites, expected",
        [
            ['Книга', ['Книга'], ['Книга']],
            ['Книга', [], []],
        ]
    )
    def test_get_list_of_favorites_books(self, collector, book, favorites, expected):
        collector.add_new_book(book)
        collector.favorites = favorites

        assert collector.get_list_of_favorites_books() == expected

    def test_get_list_of_favorites_books_empty(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 0
