from telebot import types
from MySQLCommand.get_multiple_locality import get_multiple
from Sorted.SortedBy import sorted_by

button_village = ''


def create_buttons_multiple_locality(message, bot, locality) -> None:
    """
    creates buttons of locality
    :param message: message
    :param bot: telebot
    :param locality: list
    :return: None
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in locality:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    key = types.InlineKeyboardButton(text='Показать населенные пункты заново',
                                     callback_data='Показать населенные пункты заново')
    keyboard.add(key)
    bot.send_message(message.from_user.id, text='Найдено разные населенные пункты по уездам!'
                                                '\nВыберите населенный пункт для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot, locality) -> None:
    """
    handler touch command
    :param call: callback message
    :param bot: bot
    :return:
    """
    if call.data == 'Показать населенные пункты заново':
        create_buttons_multiple_locality(call, bot, get_multiple(" ".join(map(str, locality))))
    elif "".join(map(str, locality)).strip() in call.data:
        global button_village
        button_village = call.data
        sorted_by(bot, call)
