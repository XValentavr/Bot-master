import logging
import os
import os_env
import telebot
from telebot import types

from ChatVizualization.On_chat import visualization, get_current_village
from Command import (
    CreateButtons as CreateButtons,
    Create_buttons_churches,
    Create_buttons_county,
    Create_buttoms_different_locality,
    CreateArchiveButton,
)
from Command import ForStartMenu as ForStartMenu
from Command.CreateFeadback import init_feedback
from Command.Create_buttons_churches import get_current_county
from FormCRM.RegistrationUser import init_registration
from Sorted import SortedBy

bot = telebot.TeleBot(os.getenv('TOKEN'))
logging.basicConfig(filename="sample.log", level=logging.ERROR)
village = county = {}
try:
    @bot.message_handler(commands=["info"])
    def show_info(message):
        get_current_village(message, clear=True)
        get_current_county(message, clear=True)
        bot.send_message(
            message.chat.id,
            "Ви можете знайти метрики в архівах України, використовуючи цього бота.\n"
            "1) Команда /search дозволяє Вам знайти інформації\n"
            "2) Команда /reset дозволяє Вам повернутися в початкове меню\n"
            "3) Команда /bid дозволяє Вам залишити заявку для дослідження або зв'язатися з нами",
        )


    # @bot.message_handler(commands=["help"])
    # def show_help(message):
    #   get_current_village(message, clear=True)
    #  get_current_county(message, clear=True)

    # CreateButtons.create_buttons(message, bot)

    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        get_current_village(message, clear=True)
        get_current_county(message, clear=True)

        ForStartMenu.some_action(message, bot)


    @bot.message_handler(commands=["reset"])
    def send_welcome(message):
        get_current_village(message, clear=True)
        get_current_county(message, clear=True)

        ForStartMenu.some_action(message, bot)


    # @bot.message_handler(commands=['feedback'])
    # def create_feedback(message):
    # get_current_village(message, clear=True)
    # get_current_county(message, clear=True)
    # init_feedback(bot, message)

    # @bot.message_handler(commands=["archive"])
    # def show_archive(message):
    # get_current_village(message, clear=True)
    # get_current_county(message, clear=True)

    # CreateArchiveButton.show_archive(bot, message)

    @bot.message_handler(commands=["bid"])
    def register_form(message):
        get_current_village(message, clear=True)
        get_current_county(message, clear=True)

        init_registration(bot, message)


    @bot.message_handler(commands=["search"])
    def sql_operation(message):
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(
            message.chat.id, "Введіть назву населеного пункту.", reply_markup=markup
        )
        bot.register_next_step_handler(msg, process_village)


    def process_village(message):
        visualization(message, bot)
        global village, county
        village = get_current_village(message)
        county = get_current_county(message)


    @bot.message_handler(commands=["order"])
    def process_city_step(message):
        from SendInfoToConnect.SendInfo import to_order

        to_order(message, bot)


    @bot.callback_query_handler(
        func=lambda message: message.data
                             not in ["start", "bid"]
    )
    def select_churches(message):
        cur_village = village.get(message.from_user.id)
        cur_county = county.get(message.from_user.id)

        SortedBy.callback_worker(message, bot, cur_village)
        Create_buttons_county.callback_worker(message, bot, cur_village)

        if cur_county is not None:
            Create_buttons_churches.callback_worker(message, bot, cur_village, cur_county)
        from ChatVizualization.On_chat import flag

        if flag:
            Create_buttoms_different_locality.callback_worker(message, bot)


    @bot.callback_query_handler(
        func=lambda message: message.data
                             in ["start", "bid"]
    )
    def help_handler(message):
        CreateButtons.callback_worker(message, bot)

except Exception:
    logging.basicConfig(filename="sample.log", level=logging.ERROR)

    bot.polling(none_stop=True, interval=0, allowed_updates=None)

bot.polling(none_stop=True, interval=0, allowed_updates=None)
