"""klasa Email
"""

import smtplib
import email

class Email:
    """służy do wysyałania wiadomości do wybranych osób na podstawie formularza (context menager)
    """
    def __init__(self, serwer_smtp, mail_username, mail_password):
        self.serwer = serwer_smtp
        self.port = 587
        self.username = mail_username
        self.password = mail_password
        self.object = None

    def __enter__(self):
        self.object = smtplib.SMTP(self.serwer, self.port)
        self.object.ehlo()
        self.object.starttls()
        self.object.login(self.username, self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.object.quit()

    @ staticmethod
    def _prepare_text(name, book_title):
        """przygotowuje treść maila

        Args:
            name (str): nazwa (imię) osoby do której wysyłamy wiadomość
            book_title (str): tytuł książki do oddania

        Returns:
            str: tekst wiadomości
        """
        return f'{name} przypominam Ci, że już najwyższa pora oddać mi \"{book_title}\"'

    def send_reminding_mail(self, email_, name, book_title):
        """wysyła otrzymaną treść wiadomości na wskazany adres poczty

        Args:
            send_to (str): adres email odbiorcy wiadomości.
            text (str): treść wiadomości.
        """
        text = self._prepare_text(name, book_title)
        send_to = email_
        send_from = f'Marcin K. <{self.username}>'
        #  klasa Message umożliwia zakodowanie wiadomości w utf-8 (polskie znaki)
        msg = email.message_from_string(f'From: {send_from} \nSubject: Pamiętaj \n\n{text}')
        msg.set_charset('utf-8')
        self.object.sendmail(send_from, send_to, msg.as_string())
