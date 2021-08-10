import telebot
from telebot import types  # кнопки
from Command import CreateButtons as CreateButtons, Create_buttons_churches, Create_buttons_regions, \
    Create_buttoms_new_churches
from Command import ForStartMenu as ForStartMenu
from ChatVizualization.On_chat import visualization
from ChatVizualization import On_chat
from UserRegistration.RegistrationNameUser import process_fullname_step

bot = telebot.TeleBot('1362750182:AAF8LlEm790xbapCImuE5Bd77LXp6WdEeuw')
user_dict = {}
user_dict_mysql = {}


class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone']

        for key in keys:
            self.key = None


@bot.message_handler(commands=['info'])
def show_info(message):
    bot.send_message(message.chat.id, 'This program can show you information about '
                                      'geneology and possibilities of using it')


@bot.message_handler(commands=['help'])
def show_help(message):
    CreateButtons.create_buttons(message, bot)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ForStartMenu.someAction(message, bot)


@bot.message_handler(commands=['reset'])
def send_welcome(message):
    ForStartMenu.someAction(message, bot)


@bot.message_handler(commands=['searchFor'])
def sql_operation(message):
    chat_id = message.chat.id
    user_dict_mysql[chat_id] = User(message.text)
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(chat_id, 'Введите название населенного пункта', reply_markup=markup)
    bot.register_next_step_handler(msg, process_village)


def process_village(message):
    visualization(message, bot, user_dict_mysql)


@bot.message_handler(commands=['order'])
def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Введите Имя и  Отчество', reply_markup=markup)
        bot.register_next_step_handler(msg, registration)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')


def registration(message):
    process_fullname_step(message, bot, user_dict)


@bot.callback_query_handler(func=lambda message: True)
def select_Churches(message):
    if len(On_chat.global_cities) == 0:
        On_chat.global_cities = [None for _ in range(1)]
    if On_chat.global_cities[0] is None:
        On_chat.global_cities[0] = ''
    Create_buttons_churches.callback_worker(message, bot, On_chat.global_cities, On_chat.CURRENT_CITY,
                                            On_chat.current_region)
    Create_buttons_regions.callback_worker(message, bot, On_chat.global_region, On_chat.CURRENT_CITY)
    Create_buttoms_new_churches.callback_worker(message, bot, On_chat.CURRENT_CITY)
    CreateButtons.callback_worker(message, bot)


bot.polling(none_stop=True, interval=0)
