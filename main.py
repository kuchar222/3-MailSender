"""MailSender
"""

from os import getenv
from dotenv import load_dotenv
from mail import Email
from books import Bookshelve


load_dotenv()

path = getenv('BOOKS_DB_PATH')
serwer_smtp = getenv('SERWER_SMTP')
mail_username = getenv('MAIL_USERNAME')
mail_password = getenv('MAIL_PASSWORD')

shelve = Bookshelve(path)
expired_books = shelve.find_book_to_return()
if len(expired_books) > 0:
    with Email(serwer_smtp, mail_username, mail_password) as mail:
        for book in expired_books:
            email_, name, book_title = book
            mail.send_reminding_mail(email_, name, book_title)
            print(f'Wysłano przypomnienie do {name}')
else:
    print('Na chwilę obecną nie upłynął żaden termin oddania książek')
