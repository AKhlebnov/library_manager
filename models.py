import json


class Book():
    """Класс для создания объекта книга."""

    _ID = 1

    def __init__(self, title, author, year, status='в наличии'):
        self.id = self._ID
        self.__class__._ID += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return self.title


class Library():
    """Класс для создания библиотеки."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку."""

        if any(
            b.title == book.title
            and b.author == book.author
            and b.year == book.year
            for b in self.books
        ):
            print(
                'Книга с таким же названием, автором и годом уже существует.'
            )
            return False

        self.books.append(book)
        return True

    def remove_book(self, book_id):
        """Удаляет книгу из библиотеки по её ID."""

        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                print(f'Книга с ID {book_id} удалена.')
                return True

        print(f'Книга с ID {book_id} не найдена.')
        return False

    def find_book(self, title=None, author=None, year=None):
        """Ищет книги в библиотеке по названию, автору и/или году."""

        result = []

        for book in self.books:
            if (
                (title is None or title.lower() in book.title.lower())
                and (author is None or author.lower() in book.author.lower())
                and (year is None or year == book.year)
            ):
                result.append(book)

        if not result:
            print('Книги по заданным критериям не найдены.')

        return result

    def display_books(self) -> None:
        """Выводит список всех книг в библиотеке в читаемом формате."""

        if not self.books:
            print('В библиотеке пока нет книг.')
            return

        print('Список книг:\n' + '-' * 40)

        for book in self.books:
            print(
                f'ID: {book.id} | Название: {book.title} | '
                f'Автор: {book.author} | Год: {book.year} | '
                f'Статус: {book.status}'
            )

    def change_status(self, book_id, status):
        """Меняет статус книги по её ID."""

        if status not in ('в наличии', 'выдана'):
            print('Ошибка: статус может быть только "в наличии" или "выдана".')
            return False

        for book in self.books:
            if book.id == book_id:
                book.status = status
                print(f'Статус книги с ID {book_id} изменён на "{status}".')
                return True

        print(f'Книга с ID {book_id} не найдена.')
        return False

    def save_to_file(self, filename):
        """
        Сохраняет данные библиотеки в указанный JSON-файл.
        """

        data = [
            {
             'id': book.id,
             'title': book.title,
             'author': book.author,
             'year': book.year,
             'status': book.status,
            }
            for book in self.books
        ]

        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        """
        Загружает данные библиотеки из указанного JSON-файла.
        """

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [
                    Book(
                        title=item["title"],
                        author=item["author"],
                        year=item["year"],
                        status=item["status"],
                    )
                    for item in data
                ]

        except FileNotFoundError:
            print('Файл не найден. Библиотека будет пустой.')

        except json.JSONDecodeError:
            print('Ошибка чтения файла JSON. Проверьте его содержимое.')

    def __str__(self) -> str:
        return f'Список книг библиотеки - {self.books}'
