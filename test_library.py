import unittest
from models import Book, Library


class TestBook(unittest.TestCase):
    """Тесты для класса Book."""

    def test_book_creation(self):
        """Тест создания книги."""
        book = Book("Название книги", "Автор книги", 2023)
        self.assertEqual(book.title, "Название книги")
        self.assertEqual(book.author, "Автор книги")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")

    def test_book_id_increment(self):
        """Тест автоматического увеличения ID."""
        book1 = Book("Книга 1", "Автор 1", 2023)
        book2 = Book("Книга 2", "Автор 2", 2023)
        self.assertEqual(book1.id + 1, book2.id)


class TestLibrary(unittest.TestCase):
    """Тесты для класса Library."""

    def setUp(self):
        """Инициализация библиотеки перед каждым тестом."""
        Book._ID = 1
        self.library = Library()
        self.book1 = Book("Книга 1", "Автор 1", 2023)
        self.book2 = Book("Книга 2", "Автор 2", 2024)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        """Тест добавления книги."""
        new_book = Book("Книга 3", "Автор 3", 2025)
        result = self.library.add_book(new_book)
        self.assertTrue(result)
        self.assertIn(new_book, self.library.books)

    def test_add_duplicate_book(self):
        """Тест добавления дубликата книги."""
        duplicate = Book("Книга 1", "Автор 1", 2023)
        result = self.library.add_book(duplicate)
        self.assertFalse(result)

    def test_remove_book(self):
        """Тест удаления книги."""
        result = self.library.remove_book(self.book1.id)
        self.assertTrue(result)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_nonexistent_book(self):
        """Тест удаления несуществующей книги."""
        result = self.library.remove_book(9999)
        self.assertFalse(result)

    def test_find_book(self):
        """Тест поиска книги."""
        results = self.library.find_book(title="Книга 1")
        self.assertIn(self.book1, results)
        self.assertNotIn(self.book2, results)

    def test_find_book_no_results(self):
        """Тест поиска книги, которой нет."""
        results = self.library.find_book(title="Несуществующая книга")
        self.assertEqual(results, [])

    def test_change_status(self):
        """Тест изменения статуса книги."""
        result = self.library.change_status(self.book1.id, "выдана")
        self.assertTrue(result)
        self.assertEqual(self.book1.status, "выдана")

    def test_change_status_invalid(self):
        """Тест изменения статуса на некорректный."""
        result = self.library.change_status(self.book1.id, "недоступно")
        self.assertFalse(result)
        self.assertEqual(self.book1.status, "в наличии")

    def test_save_and_load(self):
        """Тест сохранения и загрузки библиотеки."""
        self.library.save_to_file("test_library.json")
        new_library = Library()
        new_library.load_from_file("test_library.json")
        self.assertEqual(len(new_library.books), len(self.library.books))
        self.assertEqual(
            [b.title for b in new_library.books],
            [b.title for b in self.library.books]
        )


if __name__ == "__main__":
    unittest.main()
