
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
expired_books = shelve.take_book_to_return()
if len(expired_books) > 0:
    mail = Email(serwer_smtp, mail_username, mail_password)
    try:
        mail.send_reminding_mail()
        print(f'Wysłano przypomnienie do zapominalskich osób: {len(expired_books)}')
    except:
        print('Mamy problem z wysłaniem przypomnienia')
else:
    print('Na chwilę obecną nie upłynął żaden termin oddania książek')
