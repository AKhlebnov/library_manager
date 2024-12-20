# Library Manager

## Описание

Этот проект представляет собой библиотечное приложение для управления книгами. Включает функциональность добавления, удаления, поиска, изменения статуса книг и сохранения данных в файл в формате JSON. Пользователь может добавлять новые книги в библиотеку, искать книги по автору или году выпуска, а также изменять их статус.

Проект демонстрирует навыки работы с объектно-ориентированным программированием (ООП), включая создание и использование классов, методов для управления данными, а также реализации логики приложения.

## Технологии

- **Python 3.11**: основная версия Python, используемая для разработки.

## Установка

1. Клонируйте репозиторий на свой компьютер:
   ```bash
   git clone git@github.com:AKhlebnov/library_manager.git
   ```

2. Перейдите в директорию проекта:
    ```bash
    cd library_manager
    ```

3. Убедитесь, что у вас установлен Python 3.11:
    ```bash
    python --version
    ```

## Запуск приложения

Для запуска программы выполните:
    ```bash
    python main.py
    ```

Программа работает с текстовым интерфейсом, через который можно взаимодействовать с библиотекой книг.

## Тестирование

Для выполнения тестов используйте следующую команду:
    ```bash
    python -m unittest test_library.py -v
    ```

Ключ -v обеспечивает расширенный вывод, где для каждого теста будет отображаться информация о его запуске, успешности или ошибках.

## Автор

**Александр Хлебнов**
