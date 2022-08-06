"""
This module creates buttons if church mod was selected
"""

# local imports
from telebot import types

from MySQLCommand.Select_from_information_about_churches import (
    select_operation_get_churches,
)
from RegexMethods.Regex_second import generate_message

flag = True


def create_buttons_churches(message, bot, cities: list, county) -> None:
    """
    creates buttons
    :param message: message
    :param bot: telebot
    :param cities: list
    :param county: current county
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in cities:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    bot.send_message(
        message.from_user.id,
        text="Тут всі церкви по населеному пункту!"
        "\nВиберіть церкву для більшої інформації ",
        reply_markup=keyboard,
    )
    global flag
    flag = False
    get_current_county(message, county)


def get_current_county(message, county: str = None, lst_county={}):
    """
    Function stores current village
    :param village: entered village
    :param lst_county: list to store data
    :return: saved village
    """
    if county is not None:
        lst_county[message.from_user.id] = county
    return lst_county


def callback_worker(call, bot, village, county) -> None:
    """
    handler touch command
    :param call: callback message
    :param bot: bot
    :return:
    """

    cur_church = call.data.strip()
    res = select_operation_get_churches(cur_church, village, county)
    for church in res:
        reg_1 = generate_message(church)
        if len(reg_1) > 4082:
            for x in range(0, len(reg_1) - 14, 4082):
                bot.send_message(
                    call.message.chat.id, reg_1[x : x + 4082], parse_mode="Markdown"
                )
                continue
        else:
            bot.send_message(call.message.chat.id, reg_1, parse_mode="Markdown")
            continue
