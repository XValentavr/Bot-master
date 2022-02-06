"""
This module send letter to email using info from registration form
"""
import smtplib
from email.message import EmailMessage


def set_content(user_dict: dict) -> str:
    """
    This module creates message to send content
    :param user_dict: dict of user info
    :return: new created content
    """
    return f"Заявка від:\n{user_dict['name']}\n{user_dict['email']}\n+{user_dict['phone']}\n\n" \
           f"Текст повідомлення:\n{user_dict['info']}\nДата\n{user_dict['data']}"


def send_mail(user_dict: dict) -> None:
    """
    This module send email to user email
    :param user_dict: ditc of user information
    :return: None
    """
    user, password = "volynskaaoksana1973@gmail.com", "price19995"
    message = EmailMessage()
    message["Subject"] = "Бот Каталогу Метричних Книг України"
    message["From"] = 'Бот Каталогу Метричних Книг Ураїни "Генеалогія"'
    message["To"] = ['iwilly17@gmail.com']
    message.set_content(set_content(user_dict=user_dict))
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.send_message(message)
    server.quit()
