"""klasa Bookshelve
"""
import sqlite3

class Bookshelve:
    """klasa bibliteczki pobiera z bazy danych książki o określonych parametrach
    """
    def __init__(self, path) -> None:
        self.path = path
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        """tworzy połączenie z bazą danych
        """
        with sqlite3.connect(self.path) as connection:
            self.cursor = connection.cursor()

    def find_book_to_return(self):
        """pobiera książki, których termin oddania już minął

        Returns:
            list: zbiór list z danymi: email, name, book_title
        """
        self.cursor.execute(
            'SELECT email, name, book_title\
             FROM books WHERE return_at <= current_timestamp'
             )
        return list(self.cursor.fetchall())
