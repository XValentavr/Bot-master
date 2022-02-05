"""
This module creates user name
"""
import re
from FormCRM import sendletter
from datetime import date

user_dict = {"name": None, "phone": None, "email": None, "info": None, "data": None}


class Mono:
    """
    This class crete monostate pattern
    """

    __dict = {"bot": lambda instance: instance}

    def __init__(self):
        self.__dict__ = Mono.__dict


bot_value = Mono()


def init_registration(bot, message):
    """
    This module starts user registration and andle next step
    :param bot: bot API
    :param message: bot chat info
    :return: None
    """

    bot_value.bot = bot
    bot_value.bot.send_message(message.chat.id, "Введите свое имя")
    bot_value.bot.register_next_step_handler(message, register_name)


def register_name(message):
    """
    this module registrate user name and gets phone number
    :param message: bot chat information
    :return: None
    """
    try:
        name = message.text
        if len(name) and name.isalpha():
            bot_value.bot.send_message(message.chat.id, "Введите номер телефона")
            user_dict["name"] = name
            bot_value.bot.register_next_step_handler(message, register_phone)
        else:
            bot_value.bot.send_message(
                message.chat.id, "Ошибка, имя не должно содержать неподходящие символы."
            )
            bot_value.bot.send_message(message.chat.id, "Введите имя заново")
            bot_value.bot.register_next_step_handler(message, register_name)
    except Exception:
        bot_value.bot.send_message(message.chat.id, "Ошибка, попробуйте заново")


def register_phone(message):
    """
    This module registarate phone number and gets user email
    :param message: bot chat id
    :return: None
    """
    try:
        currect_number = message.text
        if currect_number.isdigit() or currect_number.startswith("+"):
            user_dict["phone"] = currect_number
            bot_value.bot.send_message(message.chat.id, "Введите свой email")
            bot_value.bot.register_next_step_handler(message, register_email)
        else:
            bot_value.bot.send_message(
                message.chat.id,
                "Вы неправильно ввели номер телефона (номер не должен содержать букв) попробуйте ещё раз",
            )
            bot_value.bot.send_message(message.chat.id, "Введите свой номер телефона")
            bot_value.bot.register_next_step_handler(message, register_phone)
    except ValueError:
        bot_value.bot.send_message(
            message.chat.id,
            "Вы неправильно ввели номер телефона (номер не должен содержать букв, попробуйте ещё раз",
        )
        register_phone(message)


def register_email(message):
    """
    This module registrates user email and gets all info
    :param message:  bot message
    :return: None
    """
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

    if re.fullmatch(regex, message.text):
        user_dict["email"] = message.text
        bot_value.bot.register_next_step_handler(message, final_register)
        bot_value.bot.send_message(message.chat.id, "Введите краткое описание")
    else:
        bot_value.bot.send_message(
            message.chat.id, "Ошибка, email не соответствует формату, попробуйте заново"
        )
        bot_value.bot.send_message(message.chat.id, "Введите свой email")

        bot_value.bot.register_next_step_handler(message, register_email)


def final_register(message):
    """
    This module finalize registration
    :param message: information about chat
    :return: None
    """
    try:
        bot_value.bot.send_message(
            message.chat.id,
            "Вы успешно зарегестрировались. С Вами свяжется наш администратор",
        )
        user_dict["info"] = message.text
        user_dict["data"] = date.today().strftime("%d/%m/%Y")
        sendletter.send_mail(user_dict)
    except Exception:
        bot_value.bot.send_message(message.chat.id, "Ошибка, попробуйте заново")
    return user_dict
