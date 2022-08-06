"""
This module shows changed data to user telegram chat
"""
# project imports

from Command.Create_buttoms_different_locality import create_buttons_multiple_locality
from MySQLCommand.MySQLSelect import SelectOperation

# local imports
from MySQLCommand.SelectChurches import get_Churches
from MySQLCommand.get_multiple_locality import get_multiple
from RegexMethods.Regex_second import generate_message
from RegexMethods.delete_if_more_than_64 import del_if_64
from Sorted import SortedBy

global_village = ""

flag = False


def visualization(message, bot) -> None:
    """
    this module transform data and send it to chat
    :param message: bot messge
    :param bot: telebot
    :return: None
    """
    village = message.text
    village = ". " + village
    global global_village
    global_village = ".*?\\" + village + "\\b.*?"

    get_current_village(message, global_village)
    _, count = get_Churches(village.strip(), " ")
    if count == 0:
        bot.send_message(
            message.chat.id, " Вибачте, нічого не знайдено.\nПеревірте дані"
        )
    if count >= 5:
        global flag
        if len(get_multiple(village)) <= 5:
            flag = False
            SortedBy.sorted_by(bot, message)
        else:
            flag = True
            village = get_multiple(village)
            create_buttons_multiple_locality(
                bot=bot, message=message, counties=del_if_64(village, len(village))
            )
    else:
        write_if_less(message, bot, village)


def write_if_less(message, bot, village):
    """
    This module writes message if church less than 5
    """
    churches = SelectOperation(village)
    for i in churches:
        messanges = generate_message(i)
        if len(messanges) > 4082:
            for x in range(0, len(messanges) - 14, 4082):
                bot.send_message(
                    message.chat.id, messanges[x: x + 4082], parse_mode="Markdown"
                )
        else:
            bot.send_message(message.chat.id, messanges, parse_mode="Markdown")


def get_current_village(message, village: str = None, lst_village={}, multiple=False, clear=False):
    """
    Function stores current village
    :param message: chat identifier
    :param village: entered village
    :param lst_village: list to store data
    :param multiple: flag if command comes from multiple village
    :return: saved village
    """

    if village is not None:
        lst_village[message.from_user.id] = village
    if multiple:
        lst_village[message.from_user.id] = village

    if clear and message.from_user.id in lst_village.keys():
        del lst_village[message.from_user.id]
    return lst_village
