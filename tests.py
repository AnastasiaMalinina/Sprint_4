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
        assert len(collector.books_genre) == 2 #исправлено наименование атрибута (Малинина А.)

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #тестирование метода add_new_book
    @pytest.mark.parametrize('name, expected_len', [
        ['',0],
        ['Ф',1],
        ['Д'*40,1],
        ['Д'*41,0]
    ])
    def test_add_new_book_add_different_len_add_one_or_zero(self, name, expected_len):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == expected_len
        
    def test_add_new_book_add_duplicate_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre == {
            'Гордость и предубеждение и зомби': 'Ужасы'
        }

    def test_add_new_book_check_genre_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    #тестирование конструктора __init__
    def test_init_check_class_attributes_exist(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    #тестирование метода set_book_genre
    @pytest.mark.parametrize('genre, expected_result', [['Ужасы', 'Ужасы'], ['Драма', '']])
    def test_set_book_genre_book_with_correct_and_incorrect_genre_expected_result(self, genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.books_genre['Гордость и предубеждение и зомби'] == expected_result

    def test_set_book_genre_no_book_name_empty_books_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        assert len(collector.books_genre) == 0

    #тестирование метода get_book_genre
    def test_get_book_genre_two_books_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Мультфильмы'
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre_nonexistent_book_return_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Идиот') is None

    #тестирование метода get_books_with_specific_genre
    @pytest.mark.parametrize('genre, expected_result', [
        ['Ужасы',['Гордость и предубеждение и зомби','Сияние']],
        ['Драма',[]]
    ])
    def test_get_books_with_specific_genre_books_with_genres_expected_result (self, genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        collector.set_book_genre('Сияние','Ужасы')
        assert collector.get_books_with_specific_genre(genre) == expected_result

    #тестирование метода get_books_genre
    def test_get_books_genre_books_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        collector.set_book_genre('Сияние','Ужасы')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби':'Ужасы', 'Что делать, если ваш кот хочет вас убить':'Мультфильмы', 'Сияние':'Ужасы'}

    #тестирование метода get_books_for_children
    def test_get_books_for_children_several_books_shows_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.add_new_book('Идиот')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        collector.set_book_genre('Сияние','Детективы')
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_books_with_age_rating_shows_nothing(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
        collector.set_book_genre('Сияние','Детективы')
        assert collector.get_books_for_children() == []

    #тестирование метода add_book_in_favorites
    def test_add_book_in_favorites_add_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert collector.favorites == ['Сияние']

    def test_add_book_in_favorites_add_non_existent_book_empty_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Идиот')
        assert collector.favorites == []

    def test_add_book_in_favorites_add_book_twice_one_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert collector.favorites == ['Сияние']

    #тестирование метода delete_book_from_favorites
    def test_delete_book_from_favorites_delete_one_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Сияние']

    #тестирование метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_full_list_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Сияние')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби','Сияние']
