"""
This module creates possibilities of sort info
"""

# local imports
from Command.Create_buttons_churches import create_buttons_churches
from telebot import types
from Command.Create_buttons_county import create_buttons_county
from MySQLCommand.SelectChurches import get_Churches


def sorted_by(bot, message) -> None:
    """
    creates buttons to sort info
    :param bot: telebot
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


def callback_worker(message, bot, village: str, county: str) -> None:
    """
    sort info bu church or county
    :param message: message
    :param bot: telebot
    :param sorted_: str
    :param village: str
    :param county: str
    :return: None
    """
    if message.data == "Церковь":
        churches, length = get_Churches(village.rstrip(), county)
        new_c = length - 1
        final_churches = [None for _ in range(length)]
        for i in churches:
            new_church = str(i)
            while (len(new_church.encode('utf-8'))) > 64:
                new_church = new_church.split()
                new_church.pop()
                new_church = ' '.join(map(str, new_church))
            final_churches[new_c] = new_church.strip()
            new_c -= 1
        create_buttons_churches(message=message, bot=bot, cities=final_churches)
    if message.data == "Уезд":
        create_buttons_county(message=message, bot=bot, village=village, county=county)
