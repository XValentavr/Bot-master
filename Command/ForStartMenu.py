from telebot import types


def some_action(message, bot):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_search = types.KeyboardButton(text='/search')
    key_info = types.KeyboardButton(text='/info')
    key_order = types.KeyboardButton(text='/order')
    key_archive = types.KeyboardButton(text='/archive')
    keyboard.add(key_search)
    keyboard.add(key_info)
    keyboard.add(key_order)
    keyboard.add(key_archive)
    bot.send_message(message.from_user.id, text='Выберите команду',
                     reply_markup=keyboard)
