"""Moduł z klasami Book i Bookshelve
"""

from datetime import date

class Book:
    def __init__(self, email, name, title, return_at) -> None:
        self.email = email
        self.name = name
        self.title = title
        self.return_at = return_at


class Bookshelve:
    def __init__(self, path) -> None:
        self.books = self.import_books_from_database(path)

    def import_books_from_database(self, path):
        books = []
        pass
        return books

    def is_return_date_expired(self, return_date):
        """sprawdza czy podana data jest starsza niż aktualna

        Args:
            date (str): data w formacie YYYY-MM-DD

        Returns:
            bool: True gdy data już minęła
        """
        return bool(date.today() >= date.fromisoformat(return_date))


