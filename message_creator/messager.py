from telebot import types

glob_to = None
glob_message = []


def message_creator(message, bot, call):
    """
    This function creates message by length of table
    :param message: message to change
    :return: message iterator
    """
    global glob_to
    message_list = []
    ms = str()
    less_than_3250 = 0
    more_then_3250 = 3250
    splitted = message.splitlines(True)
    for mes in splitted:
        if less_than_3250 + len(mes) < more_then_3250:
            ms += mes
            less_than_3250 += len(mes)
        else:
            ms += mes
            message_list.append(ms)
            ms = str()
            more_then_3250 += 3250
    else:
        message_list.append(ms)
    global glob_message
    glob_message = message_list
    if len(message_list) < 10:

        for message in message_list:
            try:
                bot.send_message(call.message.chat.id, message, parse_mode="Markdown")
            except AttributeError:
                bot.send_message(call.chat.id, message, parse_mode="Markdown")
    else:
        to_ = 10
        glob_to = to_
        for i in range(to_):
            try:
                bot.send_message(call.message.chat.id, message_list[i], parse_mode="Markdown")
            except AttributeError:
                bot.send_message(call.chat.id, message_list[i], parse_mode="Markdown")
        create_more_button(call, bot)


def call_query(call, bot):
    global glob_to
    global glob_message
    if glob_to > len(glob_message):
        glob_to = len(glob_message)
    if call.data == 'More':
        for i in range(glob_to, glob_to + 10):
            try:
                bot.send_message(call.message.chat.id, glob_message[i], parse_mode="Markdown")
            except IndexError:
                ...
        if glob_to <= len(glob_message):
            glob_to += 10
            if glob_to <= len(glob_message):
                create_more_button(call, bot, callback='query')


def create_more_button(call, bot, callback=None):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    key = types.InlineKeyboardButton(text='Показати ще', callback_data='More')
    keyboard.add(key)
    if callback is not None:
        bot.send_message(
            call.message.chat.id, text='Натисніть, щоб показати більше',
            reply_markup=keyboard, )
    else:
        try:
            bot.send_message(
                call.message.chat.id, text='Натисніть, щоб показати більше',
                reply_markup=keyboard, )
        except AttributeError:
            bot.send_message(
                call.chat.id, text='Натисніть, щоб показати більше',
                reply_markup=keyboard, )
