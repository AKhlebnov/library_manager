from exceptions import BookError, InputError
from models import Library, Book

FILENAME = 'library.json'


def display_menu():
    """Отображает меню выбора действий."""

    print("""
    Меню:
    1. Добавить книгу
    2. Удалить книгу
    3. Найти книгу
    4. Изменить статус книги
    5. Отобразить список книг
    6. Выход
    """)


def add_book_interface(library):
    """Интерфейс для добавления книги."""

    title = input('Введите название книги: ').strip()

    if not title:
        raise InputError('Название книги не может быть пустым.')

    author = input('Введите автора книги: ').strip()

    if not author:
        raise InputError('Автор книги не может быть пустым.')

    year = input('Введите год издания: ')

    try:
        year = int(year)
        if year < 1000 or year > 2100:
            raise InputError('Год издания должен быть в диапазоне 1000–2100.')
    except ValueError:
        raise InputError('Год издания должен быть числом.')

    if library.add_book(Book(title, author, year)):
        print(f'Книга "{title}" добавлена в библиотеку.')
    else:
        raise BookError(
            'Книга с таким названием, автором и годом уже существует.'
        )


def remove_book_interface(library):
    """Интерфейс для удаления книги."""

    book_id = input('Введите ID книги для удаления: ')

    try:
        book_id = int(book_id)
    except ValueError:
        raise InputError('ID должен быть числом.')

    if not library.remove_book(book_id):
        raise BookError(f'Книга с ID {book_id} не найдена.')


def find_book_interface(library):
    """Интерфейс для поиска книги."""

    title = input('Введите название книги (или оставьте пустым): ').strip()
    author = input('Введите автора книги (или оставьте пустым): ').strip()
    year = input('Введите год издания (или оставьте пустым): ')

    try:
        year = int(year) if year else None
    except ValueError:
        raise InputError('Год издания должен быть числом.')

    results = library.find_book(title=title, author=author, year=year)

    if not results:
        raise BookError('Книги по заданным критериям не найдены.')

    for book in results:
        print(book)


def change_status_interface(library):
    """Интерфейс для изменения статуса книги."""

    book_id = input('Введите ID книги: ')

    try:
        book_id = int(book_id)
    except ValueError:
        raise InputError('ID должен быть числом.')

    status = input('Введите новый статус ("в наличии" или "выдана"): ').strip()

    if status not in ('в наличии', 'выдана'):
        raise InputError('Статус может быть только "в наличии" или "выдана".')

    if not library.change_status(book_id, status):
        raise BookError(f'Книга с ID {book_id} не найдена.')


def main():
    """Основной цикл программы."""

    library = Library()

    # Автозагрузка при запуске
    print('Загрузка данных библиотеки...')
    library.load_from_file(FILENAME)

    while True:

        display_menu()
        choice = input('Выберите действие: ')

        try:
            if choice == '1':
                add_book_interface(library)
            elif choice == '2':
                remove_book_interface(library)
            elif choice == '3':
                find_book_interface(library)
            elif choice == '4':
                change_status_interface(library)
            elif choice == '5':
                library.display_books()
            elif choice == '6':
                print('Сохранение данных библиотеки...')
                library.save_to_file(FILENAME)
                print('Данные сохранены. Выход из программы.')
                break
            else:
                raise InputError('Некорректный выбор. Попробуйте снова.')
        except InputError as error:
            print(f'Ошибка ввода: {error}')
        except BookError as error:
            print(f'Ошибка книги: {error}')
        except Exception as error:
            print(f'Непредвиденная ошибка: {error}')


if __name__ == '__main__':
    main()
