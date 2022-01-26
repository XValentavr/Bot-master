from telebot import types


def create_buttons_multiple_locality(message, bot, counties) -> None:
    """
    creates buttons of locality
    :param message: message
    :param bot: telebot
    :param counties: list
    :return: None
    """

    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in counties:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    bot.send_message(message.from_user.id, text='Найдено разные населенные пункты по уездам!'
                                                '\nВыберите населенный пункт для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot) -> None:
    """
    handler touch command
    :param call: callback message
    :return:
    """
    pass
