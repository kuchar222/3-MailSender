from os import environ, getenv
from dotenv import load_dotenv

load_dotenv()
print(getenv('serwer_SMTP'))
print(getenv('MAIL_USERNAME'))