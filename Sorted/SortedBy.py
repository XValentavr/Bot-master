from Command.Create_buttons_churches import create_buttons_churches
from telebot import types
from Command.Create_buttons_county import create_buttons_county


def sorted_by(bot, message):
    keyboard = types.InlineKeyboardMarkup()
    key_church = types.InlineKeyboardButton(text='По уездам', callback_data='Уезд')
    key_county = types.InlineKeyboardButton(text='По церквям', callback_data='Церковь')
    keyboard.add(key_church)
    keyboard.add(key_county)
    bot.send_message(message.from_user.id, text='Выберите, как хотите вывести данные',
                     reply_markup=keyboard)


def callback_worker(message, bot, sorted_, village, county):
    if message.data == "Церковь":
        create_buttons_churches(message=message, bot=bot, cities=sorted_)
    if message.data == "Уезд":
        create_buttons_county(message=message, bot=bot, village=village, county=county)
