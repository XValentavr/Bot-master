"""
This module creates buttons if county mod was selected
"""

# local imports
from telebot import types
from MySQLCommand.CountyGetter import get_county
from MySQLCommand.SelectChurches import get_Churches
from Command.Create_buttons_churches import create_buttons_churches
from RegexMethods.delete_if_more_than_64 import del_if_64

global_village = ""


def create_buttons_county(message, bot, village: str) -> None:
    """
    create county buttons
    :param message: message
    :param bot: telebot
    :param village: list
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    village = "".join(map(str, village))
    counties = get_county(village, " ")
    for i in counties:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    bot.send_message(
        message.from_user.id,
        text="Здесь все уезды по указанному городу!"
        "\nВыберите команду для большей информации ",
        reply_markup=keyboard,
    )
    global global_village
    global_village = village


def callback_worker(call, bot) -> None:
    """
    handle touch command
    :param call: message call
    :param bot: telebot
    :return: None
    """
    if "повіт" in call.data:
        village = "".join(map(str, global_village))
        counties, counter = get_Churches(village, call.data)
        create_buttons_churches(
            call, bot, del_if_64(counties, counter), village, call.data
        )
