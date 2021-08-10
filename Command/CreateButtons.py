from telebot import types

help = ['Получаем информацию о всех командах']
start = ['Начало работы проекта']
searchFor = ['Поиск информации']
info_first = ['Получить информацию о возможностях']


def create_buttons(message, bot):
    keyboard = types.InlineKeyboardMarkup()
    key_start = types.InlineKeyboardButton(text='/start', callback_data='start')
    key_help = types.InlineKeyboardButton(text='/help', callback_data='help')
    key_info_first = types.InlineKeyboardButton(text='/info', callback_data='info_first')
    keyboard.add(key_start)
    keyboard.add(key_help)
    keyboard.add(key_info_first)
    bot.send_message(message.from_user.id, text='Здесь все команды!'
                                                '\nВыберите команду для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot):
    if call.data == 'help':
        msg = help
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'start':
        msg = start
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'info_first':
        msg = info_first
        bot.send_message(call.message.chat.id, msg)
