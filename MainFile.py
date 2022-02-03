import telebot
from telebot import types
from Command import (
    CreateButtons as CreateButtons,
    Create_buttons_churches,
    Create_buttons_county,
    Create_buttoms_different_locality,
    CreateArchiveButton,
)
from Command import ForStartMenu as ForStartMenu
from ChatVizualization.On_chat import visualization
from FormCRM.RegistrationUser import init_registration
from Sorted import SortedBy

bot = telebot.TeleBot("1362750182:AAF8LlEm790xbapCImuE5Bd77LXp6WdEeuw")
user_dict_mysql = {}


@bot.message_handler(commands=["info"])
def show_info(message):
    bot.send_message(
        message.chat.id,
        "Вы можете найти метрики в архивах Украины, используя этого бота.",
    )


@bot.message_handler(commands=["help"])
def show_help(message):
    CreateButtons.create_buttons(message, bot)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    ForStartMenu.some_action(message, bot)


@bot.message_handler(commands=["reset"])
def send_welcome(message):
    ForStartMenu.some_action(message, bot)


@bot.message_handler(commands=["archive"])
def show_arcive(message):
    CreateArchiveButton.show_archive(bot, message)


@bot.message_handler(commands=["form"])
def register_form(message):
    init_registration(bot, message)


@bot.message_handler(commands=["search"])
def sql_operation(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(
        chat_id, "Введите название населенного пункта", reply_markup=markup
    )
    bot.register_next_step_handler(msg, process_village)


def process_village(message):
    visualization(message, bot)


@bot.message_handler(commands=["order"])
def process_city_step(message):
    from SendLetter.SendLetter import to_order

    to_order(message, bot)


@bot.callback_query_handler(
    func=lambda message: message.data not in ["help", "start", "info_first", "archive", "form"]
)
def select_churches(message):
    SortedBy.callback_worker(message, bot)
    Create_buttons_county.callback_worker(message, bot)
    Create_buttons_churches.callback_worker(message, bot)
    from ChatVizualization.On_chat import flag

    if flag:
        Create_buttoms_different_locality.callback_worker(message, bot)


@bot.callback_query_handler(
    func=lambda message: message.data in ["help", "start", "info_first", "archive", "form"]
)
def help_handler(message):
    CreateButtons.callback_worker(message, bot)


bot.polling(none_stop=True, interval=0, allowed_updates=None)
