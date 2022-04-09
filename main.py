from os import getenv
from dotenv import load_dotenv
from books import Bookshelve

load_dotenv()


if __name__ == '__main__':
    shelve = Bookshelve(getenv('BOOKS_DB_PATH'))
