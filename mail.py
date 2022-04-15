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
        self.smptObj = None

    def __enter__(self):
        self.smptObj = smtplib.SMTP(self.serwer, self.port)
        self.smptObj.ehlo()  # tu jest sprawdzanie połaczenie powinna być odpowiedź: self.smptObj.ehlo()[0] == 250
        self.smptObj.starttls()
        self.smptObj.login(self.username, self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.smptObj.quit()

    def _prepare_text(self, name, book_title):
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
        msg = email.message_from_string(f'From: {send_from} \nSubject: Pamiętaj \n\n{text}')
        msg.set_charset('utf-8')
        self.smptObj.sendmail(send_from, send_to, msg.as_string())
