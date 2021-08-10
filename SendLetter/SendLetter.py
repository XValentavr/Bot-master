import smtplib


def create_email(msg, new_user_dict):
    messange = f"ФИО: {str(new_user_dict.fullname)}, номер телефона: {str(new_user_dict.phone)}"
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("xa11867787@student.karazin.ua", "price19995")
    server.sendmail("xa11867787@student.karazin.ua", "iwilly17@gmail.com",
                    messange.encode('utf-8'))
    server.quit()
