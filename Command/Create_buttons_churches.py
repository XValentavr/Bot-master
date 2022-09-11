"""
This module creates buttons if church mod was selected
"""

# local imports
from telebot import types
from difflib import SequenceMatcher
import message_creator.messager
from MySQLCommand.Select_from_information_about_churches import (
    select_operation_get_churches,
)
from RegexMethods.Regex_second import generate_message

flag = True


def create_buttons_churches(message, bot, churches: list, county) -> None:
    """
    creates buttons
    :param message: message
    :param bot: telebot
    :param churches: list
    :param county: current county
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i, _ in enumerate(churches):
        try:
            print(churches[i])
            s = SequenceMatcher(None, churches[i].replace('церква', ''), churches[i + 1].replace('церква', ''))
            print(s.ratio())
        except IndexError:
            break
    for i in churches:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    bot.send_message(
        message.from_user.id,
        text="Знайшов метричні книги таких церков населеного пункту.\n"
             "Виберіть церкву, щоб отримати більше даних",
        reply_markup=keyboard,
    )
    global flag
    flag = False
    get_current_county(message, county)


def get_current_county(message, county: str = None, dct_county={}, clear=False):
    """
    Function stores current county
    :param county: entered county
    :param dct_county: list to store data
    :param message: chat identifier
    :param clear: flag if command is clear dict of data
    :return: saved village
    """
    if county is not None:
        dct_county[message.from_user.id] = county

    if clear and message.from_user.id in dct_county.keys():
        del dct_county[message.from_user.id]
    return dct_county


def callback_worker(call, bot, village, county) -> None:
    """
    handler touch command
    :param call: callback message
    :param bot: bot
    :param village: current village to get info
    :param county: county that village belongs to
    :return:
    """

    cur_church = call.data.strip()
    res = select_operation_get_churches(cur_church, village, county)
    for church in res:
        reg_1 = generate_message(church)
        if len(reg_1) > 4082:
            message_creator.messager.message_creator(reg_1, bot, call)
        else:
            bot.send_message(call.message.chat.id, f"{generate_message(church)}", parse_mode="Markdown")
            continue
