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
    global global_village
    global_village = village
    _, count = get_Churches(village.strip(), " ")
    if count == 0:
        bot.send_message(
            message.chat.id, " Извините, ничего не найдено.\nПроверьте данные"
        )
    if count >= 5:
        global flag
        if len(get_multiple(village)) <= 5:
            flag = False
            village = ".*?\\" + village + "\\b.*?"
            SortedBy.sorted_by(bot, message, village)
        else:

            flag = True
            create_buttons_multiple_locality(
                bot=bot, message=message, counties=get_multiple(village)
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
