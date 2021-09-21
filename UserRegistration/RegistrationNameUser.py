'''from . import RegistrationNumber

global bot_value
global new_user_dict


def process_fullname_step(message, bot, user_dict):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text
        msg = bot.send_message(chat_id, 'Ваш номер телефона ')
        bot.register_next_step_handler(msg, get_phone_number)

        global bot_value
        bot_value = bot
        global new_user_dict
        new_user_dict = user_dict

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def get_phone_number(message):
    RegistrationNumber.process_phone_step(message, bot_value, new_user_dict)'''
