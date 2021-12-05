"""
This module creates buttons if county mod was selected
"""

# local imports
from telebot import types
from MySQLCommand.CountyGetter import get_county
from MySQLCommand.SelectChurches import get_Churches
from Command.Create_buttons_churches import create_buttons_churches


def create_buttons_county(message, bot, village: list, county: str) -> None:
    """
    create county buttons
    :param message: message
    :param bot: telebot
    :param village: list
    :param county: str
    :return: None
    """
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    village = "".join(map(str, village))
    counties = get_county('. ' + village, county)
    for i in counties:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    key = types.InlineKeyboardButton(text='Показать уезды заново', callback_data='Показать уезды заново')
    keyboard.add(key)
    bot.send_message(message.from_user.id, text='Здесь все уезды по указанному городу!'
                                                '\nВыберите команду для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot, village: list, county: str) -> None:
    """
    handle touch command
    :param call: message call
    :param bot: telebot
    :param village: list
    :param county: str
    :return: None
    """
    village = " ".join(map(str, village))
    if 'повіт' in call.data:
        village = "".join(map(str, village))
        counties, counter = get_Churches('. ' + village, call.data)
        global_counties = [None for _ in range(counter)]
        counter -= 1
        for county in counties:
            global_counties[counter] = county
            counter -= 1
        new_c = counter
        final_global_counties = [None for _ in range(len(global_counties))]
        for i in global_counties:
            new_county = str(i)
            while (len(new_county.encode('utf-8'))) > 64:
                new_county = new_county.split()
                new_county.pop()
                new_county = ' '.join(map(str, new_county))
            final_global_counties[new_c] = new_county.strip()
            new_c -= 1
        create_buttons_churches(call, bot, final_global_counties)
    if call.data == 'Показать уезды заново':
        create_buttons_county(call, bot, village, county)
