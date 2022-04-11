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


    def send_reminding_mail(self, send_to, text):
        """wysyła otrzymaną treść wiadomości na wskazany adres poczty

        Args:
            send_to (str): adres email odbiorcy wiadomości.
            text (str): treść wiadomości.
        """
        send_from = self.username
        msg = f'From: Przypominacz \nSubject: Pamiętaj \n\n{text}'

        smptObj = smtplib.SMTP(self.serwer, 587)
        smptObj.ehlo()  # tu jest sprawdzanie połaczenie powinna być odpowiedź: smptObj.ehlo()[0] == 250
        smptObj.starttls()
        smptObj.login(self.username, self.password)
        smptObj.sendmail(send_from, send_to, msg)
        smptObj.quit()
