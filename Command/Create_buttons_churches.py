"""
This module creates buttons if church mod was selected
"""

# local imports
from telebot import types
from MySQLCommand.Select_from_information_about_churches import (
    select_operation_get_churches,
)
from RegexMethods.Regex_second import generate_message

global_village = ""
global_county = ""


def create_buttons_churches(message, bot, cities: list, village, county) -> None:
    """
    creates buttons
    :param message: message
    :param bot: telebot
    :param cities: list
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in cities:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    bot.send_message(
        message.from_user.id,
        text="Здесь все церкви по указанному городу!"
        "\nВыберите команду для большей информации ",
        reply_markup=keyboard,
    )
    global global_county
    global_county = county

    global global_village
    global_village = village


def callback_worker(call, bot) -> None:
    """
    handler touch command
    :param call: callback message
    :param bot: bot
    :return:
    """

    cur_church = call.data.strip()
    res = select_operation_get_churches(cur_church, global_village, global_county)
    for church in res:
        reg_1 = generate_message(church)
        if len(reg_1) > 4096:
            for x in range(0, len(reg_1), 4096):
                bot.send_message(
                    call.message.chat.id, reg_1[x : x + 4096], parse_mode="Markdown"
                )
                continue
        else:
            bot.send_message(call.message.chat.id, reg_1, parse_mode="Markdown")
            continue
