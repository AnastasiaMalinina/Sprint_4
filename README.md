# qa\_python



Описание реализованных тестов



В тестовом классе TestBooksCollector реализованы проверки основных методов класса BooksCollector.



1\. Тестирование метода add\_new\_book:

* test\_add\_new\_book\_add\_different\_len\_add\_one\_or\_zero - проверка ограничений на длину названия книги (применена параметризация)                
* test\_add\_new\_book\_add\_duplicate\_one\_book - проверка на отсутствие дубликатов и сохранение ранее установленного жанра     
* test\_add\_new\_book\_check\_genre\_no\_genre - проверка на то, что в случае не установки жанра, жанр будет отсутствовать



2\. Тестирование конструктора \_\_init\_\_:

* test\_init\_check\_class\_attributes\_exist - проверка корректного создания пустого словаря книг, пустого списка избранного и заполнения списков жанров

&#x20;       

3\. Тестирование метода set\_book\_genre:

* test\_set\_book\_genre\_book\_with\_correct\_and\_incorrect\_genre\_expected\_result - проверка установки допустимого жанра, отклонения недопустимого жанра (применена параметризация)
* test\_set\_book\_genre\_no\_book\_name\_empty\_books\_genre - проверка невозможности установить жанр несуществующей книге



4\. Тестирование метода get\_book\_genre:

* test\_get\_book\_genre\_two\_books\_get\_genre - проверка возврата установленного жанра
* test\_get\_book\_genre\_nonexistent\_book\_return\_none - проверка обработки запроса для несуществующей книги

&#x20;       

5\. Тестирование метода get\_books\_with\_specific\_genre:

* test\_get\_books\_with\_specific\_genre\_books\_with\_genres\_expected\_result - проверка формирования списка книг с заданным жанром, в том числе для недопустимого жанра (применена параметризация)



6\. Тестирование метода get\_books\_genre:

* test\_get\_books\_genre\_books\_full\_dictionary - проверка возврата полного словаря с добавленными книгами и их жанрами

&#x20;       

7\. Тестирование метода get\_books\_for\_children:

* test\_get\_books\_for\_children\_several\_books\_shows\_books\_for\_children - проверка вывода книг для детей
* test\_get\_books\_for\_children\_books\_with\_age\_rating\_shows\_nothing - проверка исключения книг с возрастными ограничениями



8\. Тестирование метода add\_book\_in\_favorites:

* test\_add\_book\_in\_favorites\_add\_book\_success - проверка добавления существующих книг
* test\_add\_book\_in\_favorites\_add\_non\_existent\_book\_empty\_favorites - проверка игнорирования несуществующих книг
* test\_add\_book\_in\_favorites\_add\_book\_twice\_one\_book\_in\_favorites - проверка предотвращения повторного добавления существующих книг

&#x20;       

9\. Тестирование метода delete\_book\_from\_favorites:

* test\_delete\_book\_from\_favorites\_delete\_one\_book\_success - проверка удаления выбранной книги из списка

&#x20;       

10\. Тестирование метода get\_list\_of\_favorites\_books:

* test\_get\_list\_of\_favorites\_books\_full\_list\_success - проверка возврата списка добавленных в избранное книг





