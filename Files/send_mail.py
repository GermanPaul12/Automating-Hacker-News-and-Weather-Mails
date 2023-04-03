import yagmail
from .. import secret

def send_email(to, subject, message):
    sender = yagmail.SMTP(user=secret.MAIL_EMAIL, password=secret.MAIL_PW)
    sender.send(to=to, subject=subject, contents=message)