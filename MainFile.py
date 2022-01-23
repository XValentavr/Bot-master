import telebot
from telebot import types
from Command import CreateButtons as CreateButtons, Create_buttons_churches, Create_buttoms_different_locality
from Command import ForStartMenu as ForStartMenu
from ChatVizualization.On_chat import visualization
from ChatVizualization import On_chat
from Sorted import SortedBy
from Command import Create_buttons_county

bot = telebot.TeleBot('1362750182:AAF8LlEm790xbapCImuE5Bd77LXp6WdEeuw')
user_dict_mysql = {}


@bot.message_handler(commands=['info'])
def show_info(message):
    bot.send_message(message.chat.id, 'Вы можете найти метрики в архивах Украины, используя этого бота.')


@bot.message_handler(commands=['help'])
def show_help(message):
    CreateButtons.create_buttons(message, bot)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ForStartMenu.someAction(message, bot)


@bot.message_handler(commands=['reset'])
def send_welcome(message):
    ForStartMenu.someAction(message, bot)


@bot.message_handler(commands=['search'])
def sql_operation(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(chat_id, 'Введите название населенного пункта', reply_markup=markup)
    bot.register_next_step_handler(msg, process_village)


def process_village(message):
    visualization(message, bot)


@bot.message_handler(commands=['order'])
def process_city_step(message):
    try:
        from SendLetter.SendLetter import to_order
        to_order(message, bot)

    except Exception:
        bot.reply_to(message, 'Произошла ошибка. Перезапустите бота.')


@bot.callback_query_handler(func=lambda message: True)
def select_churches(message):
    if len(On_chat.global_cities) == 0:
        On_chat.global_cities = [None for _ in range(1)]
    if On_chat.global_cities[0] is None:
        On_chat.global_cities[0] = ' '
    Create_buttoms_different_locality.callback_worker(message, bot, On_chat.CURRENT_CITY)
    from Command.Create_buttoms_different_locality import button_village
    if button_village != '' and "".join(map(str, On_chat.CURRENT_CITY)).strip() in "".join(
            map(str, button_village)).strip():
        village = button_village
    else:
        village = '. ' + "".join(map(str, On_chat.CURRENT_CITY)).strip()
    SortedBy.callback_worker(message, bot, village, On_chat.current_region)
    Create_buttons_churches.callback_worker(message, bot, On_chat.global_cities, village,
                                            On_chat.current_region)
    Create_buttons_county.callback_worker(message, bot, village, On_chat.current_region)
    CreateButtons.callback_worker(message, bot)


bot.polling(none_stop=True, interval=0, allowed_updates=None)
