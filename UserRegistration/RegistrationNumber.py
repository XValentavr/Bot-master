"""
This module registrate user phine number
"""


'''from UserRegistration import RegistrationNameUser
from SendLetter.SendLetter import to_order

global bot_value
global new_user_dict


def process_phone_step(message, bot, user_dict:dict)->None:
    """
    Registrate phone number in a dict
    :param message:message
    :param bot:telebot
    :param user_dict:dict
    :return:None
    """
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text
        global new_user_dict
        new_user_dict = user
        global bot_value
        bot_value = bot
        if user.phone.isdigit():
            msg = bot.send_message(chat_id, 'Вы успешно зарегестрировались! С Вами свяжется администратор')
            to_order(message, bot, new_user_dict)
        else:
            msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
            bot.register_next_step_handler(msg, RegistrationNameUser.get_phone_number)
    except Exception as e:
        print('Проиизошла ошибка, повторите попытку запроса:', e)
'''
