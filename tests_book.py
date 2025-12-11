from main import BooksCollector
import pytest

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
   
    # проверка первоначального состояния
    def test_initial_state(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {} and collector.get_list_of_favorites_books() == []

        # проверка добавления книги в словарь без жанра
    def test_add_new_book_correct_add_book_successful_add(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        assert collector.get_book_genre('Диалоги.') == ''
   
    # проверка добавления книги с количеством букв в названии более 40.
    def test_add_new_book_more_forty_simbol(self):
        collector = BooksCollector()
        collector.add_new_book('Спасение утопающих дело рук самих утопающих.')
        assert collector.get_books_genre() == {}
    
    #  проверка на успешное присвоение жанра из списка ganre.
    def test_set_book_genre_correct_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        collector.set_book_genre('Диалоги.', 'Фантастика')
        assert collector.books_genre['Диалоги.'] == 'Фантастика'

    # проверка получения жанра книги по её имени.
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        collector.set_book_genre('Диалоги.', 'Фантастика')
        assert collector.get_book_genre('Диалоги.') == 'Фантастика'

    # проверка жанр не входящий в список не устанавливается.
    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        collector.set_book_genre('Диалоги.', 'FFFFFF')
        assert collector.books_genre['Диалоги.'] == ''

    # проверка получения книг по жанрам
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        collector.set_book_genre('Диалоги.', 'Фантастика')
        assert collector.get_book_genre('Диалоги.') == 'Фантастика'

    # параметризированная проверка неуспешного добавления книг.
    @pytest.mark.parametrize("name", ['', 'Спасение утопающих дело рук самих утопающих.'])
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # проверка получения текущего словаря books_genre.
    def test_get_books_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Диалоги.')
        collector.set_book_genre('Диалоги.', 'Фантастика')
        assert collector.get_book_genre('Диалоги.') == 'Фантастика'







    
