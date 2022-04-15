"""klasa Email 
"""

import smtplib

class Email:
    """służy do wysyałania wiadomości do wybranych osób na podstawie formularza
    """
    def __init__(self, serwer_smtp, mail_username, mail_password):
        self.serwer = serwer_smtp
        self.username = mail_username
        self.password = mail_password

    def _prepare_text(self, name, book_title):
        return f'{name} przypominam Ci, że już najwyższa pora oddać mi {book_title}'.encode('utf-8')

    def send_reminding_mail(self, email, name, book_title):
        """wysyła otrzymaną treść wiadomości na wskazany adres poczty

        Args:
            send_to (str): adres email odbiorcy wiadomości.
            text (str): treść wiadomości.
        """
        text = self._prepare_text(name, book_title)
        send_to = email
        send_from = self.username
        msg = f'From: {send_from} \nSubject: Pamietaj \n\n{text}'

        smptObj = smtplib.SMTP(self.serwer, 587)
        smptObj.ehlo()  # tu jest sprawdzanie połaczenie powinna być odpowiedź: smptObj.ehlo()[0] == 250
        smptObj.starttls()
        smptObj.login(self.username, self.password)
        smptObj.sendmail(send_from, send_to, msg)
        smptObj.quit()
