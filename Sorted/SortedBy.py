"""
This module creates possibilities of sort info
"""

from telebot import types

# local imports
from Command.Create_buttons_churches import create_buttons_churches
from Command.Create_buttons_county import create_buttons_county
from MySQLCommand.SelectChurches import get_Churches
from RegexMethods.delete_if_more_than_64 import del_if_64


def sorted_by(bot, message) -> None:
    """
    create sorted buttons
    :param bot: bot token
    :param message: message from user
    :return:
    """
    keyboard = types.InlineKeyboardMarkup()
    key_church = types.InlineKeyboardButton(text="По повітам", callback_data="Уезд")
    key_county = types.InlineKeyboardButton(text="По церквам", callback_data="Церковь")
    keyboard.add(key_church)
    keyboard.add(key_county)
    bot.send_message(
        message.from_user.id,
        text="Виберіть, як Ви хочете вивести дані",
        reply_markup=keyboard,
    )


def callback_worker(message, bot, village):
    """
    sort info by church or county
    :return: None
    """
    print(village)
    if message.data == "Церковь":
        churches, length = get_Churches(village.strip(), " ")
        create_buttons_churches(
            message=message,
            bot=bot,
            cities=del_if_64(churches, length),
            county=" ",
        )
    elif message.data == "Уезд":
        create_buttons_county(message=message, bot=bot, village=village)
