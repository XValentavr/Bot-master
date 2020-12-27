import re

from telebot import types

from Command.Create_buttoms_new_churches import create_buttons_new_churches
from Command.Create_buttons_churches import create_buttons_churches
from MySQLCommand.ChurchesCounter import get_Churches_counter
from MySQLCommand.SelectChurches import get_Churches
from MySQLCommand.Select_from_information_about_churches import SelectOperation
from RegexMethods.Regex_second import get_regex

call_data = ''

def create_buttons_regions(message, bot, regions, cur_city):
    cur_city = " ".join(map(str, cur_city))
    keyboard = types.InlineKeyboardMarkup()
    for i in regions:
        key = types.InlineKeyboardButton(text=cur_city + ' ' + i, callback_data=i)
        keyboard.add(key)
    key = types.InlineKeyboardButton(text='Показать заново населенные пункты',
                                     callback_data='Показать заново населенные пункты')
    keyboard.add(key)
    bot.send_message(message.from_user.id, text='Здесь все  города!'
                                                '\nВыберите команду для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot, regions, current_region):
    cur_regions = " ".join(map(str, current_region))
    new_count = get_Churches_counter('. ' + cur_regions, call.data)
    global_cities = [None for i in range(new_count)]
    c = new_count - 1
    if new_count >= 5:
        churches = get_Churches('. '+cur_regions, call.data)
        for church in churches:
            zero = church[0].split()
            if zero[0] == 'церква':
                new_church = " ".join(map(str, church))
                new_church = re.sub('\(.*', '', new_church, flags=re.DOTALL)
                new_church = re.sub(',.*', '', new_church, flags=re.DOTALL)
            else:
                new_church = " ".join(map(str, church))
                new_church = re.sub('церква.*', '', new_church, flags=re.DOTALL)
            if (len(new_church.encode('utf-8'))) > 64:
                new_i = ''.join(map(str, new_church)).split()[:-1]
                new_i.pop(0)
                global_cities[c] = ' '.join(map(str, new_i))
            elif (new_church[-1] == '.'):
                global_cities[c] = (new_church + ' ')
            else:
                if zero[0] != 'церква':
                    if (len(new_church.encode('utf-8'))) < 51:
                        new_church = new_church + 'церква'
                global_cities[c] = new_church
            c -= 1
        cur_region = call.data
        create_buttons_new_churches(call, bot, global_cities, cur_region)
    else:
        for i in regions:
            if call.data == i:
                res = SelectOperation(call.data, '. ' + cur_regions, call.data)
                for i in res:
                    reg_1 = get_regex(i)
                    if len(reg_1) > 4096:
                        for x in range(0, len(reg_1), 4096):
                            bot.send_message(call.message.chat.id, reg_1[x:x + 4096], parse_mode='Markdown')
                            continue
                    else:
                        bot.send_message(call.message.chat.id, reg_1, parse_mode='Markdown')
                        continue

    if call.data == 'Показать заново населенные пункты':
        create_buttons_regions(call, bot, regions, cur_regions)
