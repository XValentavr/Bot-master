from telebot import types

from Sorted.SortedBy import sorted_by


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
    bot.send_message(
        message.from_user.id,
        text="Знайдено різні населені пункти по повітам!"
             "\nВиберіть населений пункт для більшої інформації.",
        reply_markup=keyboard,
    )


def callback_worker(call, bot) -> None:
    """
    handler touch command
    :param call: callback message
    :param bot:bot polling
    :return:
    """
    from ChatVizualization.On_chat import get_current_village

    village = ''.join(filter(str.isalpha, get_current_village(call).get(call.from_user.id).strip()))
    if village.replace('b', '') in call.data:
        get_current_village(message=call, village=call.data, multiple=True)
        sorted_by(bot, call)
