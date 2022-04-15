"""Moduł z klasą Bookshelve
"""
import sqlite3

class Bookshelve:
    """klasa bibliteczki pobiera z bazydanych książki o określonych parametrach
    """
    def __init__(self, path) -> None:
        with sqlite3.connect(path) as connection:
            self.cursor = connection.cursor()

    def find_book_to_return(self):
        """pobiera książki, których termin oddania już minął

        Returns:
            list: zbiór list z danymi: email, name, book_title
        """
        self.cursor.execute('SELECT email, name, book_title FROM books WHERE return_at <= current_timestamp')
        return [book for book in self.cursor.fetchall()]
