import smtplib
from email.mime.text import MIMEText
from email.header import Header


def create_email(new_user_dict):
    mailsender = smtplib.SMTP('smtp.gmail.com', 587)
    mailsender.starttls()
    mailsender.login('xa11867787@student.karazin.ua', 'price19995')
    mail_recipient = 'iwilly17@gmail.com'
    mail_subject = 'Вопрос по исследованию'
    mail_body = 'ФИО {}, номер телефона {}'.format(new_user_dict.fullname, new_user_dict.phone)
    msg = MIMEText(mail_body, 'plain', 'utf-8')
    msg['Subject'] = Header(mail_subject, 'utf-8')
    mailsender.sendmail('Адрес почты отправителя', mail_recipient, msg.as_string())
    mailsender.quit()
