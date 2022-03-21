"""
This module shows posibilities of command of bot
"""

# local imports
from telebot import types

help = ["Отримуємо інформацію про всі команди"]
start = ["Початок роботи бота"]
searchFor = ["Пошук інформації"]
info_first = ["Отримати інформацію про можливості"]
archive = ["Отримати місцезнаходження архіву та поштовий адрес"]
form = ["Залишити заяву для дослідження"]


def create_buttons(message, bot) -> None:
    """
    create inline buttons to show more info
    :param message: message
    :param bot: telebot
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup()
    key_start = types.InlineKeyboardButton(text="/start", callback_data="start")
    key_help = types.InlineKeyboardButton(text="/help", callback_data="help")
    key_info_first = types.InlineKeyboardButton(
        text="/info", callback_data="info_first"
    )
    key_archive = types.InlineKeyboardButton(text="/archive", callback_data="archive")
    key_form = types.InlineKeyboardButton(text="/form", callback_data="form")
    keyboard.add(key_start)
    keyboard.add(key_help)
    keyboard.add(key_info_first)
    keyboard.add(key_archive)
    keyboard.add(key_form)
    bot.send_message(
        message.from_user.id,
        text="Тут всі команди!" "\nВиберіть команду для отримання інформації",
        reply_markup=keyboard,
    )


def callback_worker(call, bot) -> None:
    """
    handle touch command
    :param call: call message
    :param bot: telebot
    :return: None
    """
    if call.data == "help":
        bot.send_message(call.message.chat.id, help)
    elif call.data == "start":
        bot.send_message(call.message.chat.id, start)
    elif call.data == "info_first":
        bot.send_message(call.message.chat.id, info_first)
    elif call.data == "archive":
        bot.send_message(call.message.chat.id, archive)
    elif call.data == "form":
        bot.send_message(call.message.chat.id, form)
