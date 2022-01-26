"""
This module creates possibilities of sort info
"""

# local imports
from Command.Create_buttons_churches import create_buttons_churches
from telebot import types
from Command.Create_buttons_county import create_buttons_county
from MySQLCommand.SelectChurches import get_Churches
from RegexMethods.delete_if_more_than_64 import del_if_64

global_village = ''


def sorted_by(bot, message, village: str) -> None:
    """
    creates buttons to sort info
    :param message: message
    :return:
    """
    keyboard = types.InlineKeyboardMarkup()
    key_church = types.InlineKeyboardButton(text='По уездам', callback_data='Уезд')
    key_county = types.InlineKeyboardButton(text='По церквям', callback_data='Церковь')
    keyboard.add(key_church)
    keyboard.add(key_county)
    bot.send_message(message.from_user.id, text='Выберите, как хотите вывести данные',
                     reply_markup=keyboard)
    global global_village
    global_village = village


def callback_worker(message, bot):
    """
    sort info by church or county
    :return: None
    """
    if message.data == "Церковь":
        churches, length = get_Churches(global_village.strip(), ' ')
        create_buttons_churches(message=message, bot=bot, cities=del_if_64(churches, length),
                                village=global_village, county=' ')
    if message.data == "Уезд":
        create_buttons_county(message=message, bot=bot, village=global_village)
