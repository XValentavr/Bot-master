from telebot import types


def some_action(message, bot):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    key_search = types.KeyboardButton(text="/search")
    key_info = types.KeyboardButton(text="/info")
    key_form = types.KeyboardButton(text="/bid")

    keyboard.add(key_search)
    keyboard.add(key_info)
    keyboard.add(key_form)
    bot.send_message(
        message.from_user.id,
        text="Вітаю! Я генеалогічний бот Тарас. Допомагаю дізнатися, які метричні книги є в архівах України."
        " Оберіть команду, щоб я почав працювати.",
        reply_markup=keyboard,
    )
