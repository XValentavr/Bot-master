from telebot import types


def someAction(message, bot):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_searchfor = types.KeyboardButton(text='/searchFor')
    key_info = types.KeyboardButton(text='/info')
    key_order = types.KeyboardButton(text='/order')

    keyboard.add(key_searchfor)
    keyboard.add(key_info)
    keyboard.add(key_order)
    bot.send_message(message.from_user.id, text='Выберите команду',
                     reply_markup=keyboard)
