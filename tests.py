import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    for genre in collector.genre:
        name = f"Книга - {genre}"
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector

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

    def test_set_book_genre(self):
        collector = BooksCollector()

        name = 'Книга'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''
        genre = collector.genre[0]

        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_book(self):
        collector = BooksCollector()

        name = 'Книга'
        genre = collector.genre[0]

        collector.set_book_genre(name, genre)
        assert not collector.get_book_genre(name)

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()

        name = 'Книга'
        collector.add_new_book(name)
        genre = 'Жанр'

        collector.set_book_genre(name, genre)
        assert not collector.get_book_genre(name)

    def test_get_books_with_specific_genre(self, collector):
        for genre in collector.genre:
            books = collector.get_books_with_specific_genre(genre)
            assert len(books) == 1
            assert books[0] == f"Книга - {genre}"

    def test_get_books_genre(self):
        collector = BooksCollector()
        name = 'Книга'
        collector.add_new_book(name)
        genre = collector.genre[0]

        collector.set_book_genre(name, genre)
        books = collector.get_books_genre()
        assert len(books.keys()) == 1
        assert books.get(name) == genre

    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert not collector.get_books_genre()

    def test_get_books_for_children(self, collector):
        books = collector.get_books_for_children()

        for name, genre in collector.books_genre.items():
            if genre in collector.genre_age_rating:
                assert name not in books
            else:
                assert name in books

    def test_get_books_for_children_empty(self):
        collector = BooksCollector()
        assert not collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector):
        assert not collector.get_list_of_favorites_books()

        for name in collector.books_genre.keys():
            collector.add_book_in_favorites(name)
            assert name in collector.get_list_of_favorites_books()

            collector.delete_book_from_favorites(name)
            assert name not in collector.get_list_of_favorites_books()

        assert not collector.get_list_of_favorites_books()
        collector.add_book_in_favorites("yandex")
        assert not collector.get_list_of_favorites_books()
