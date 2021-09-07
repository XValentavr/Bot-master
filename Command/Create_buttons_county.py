from telebot import types
from RegexMethods.Regex_second import generate_message
from MySQLCommand.CountyGetter import get_county
from MySQLCommand.Select_from_information_about_counties import select_operation_get_counties


def create_buttons_county(message, bot, village, county):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    village = " ".join(map(str, village))
    counties = get_county('. ' + village, county)
    for i in counties:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    key = types.InlineKeyboardButton(text='Показать уезды заново', callback_data='Показать уезды заново')
    keyboard.add(key)
    bot.send_message(message.from_user.id, text='Здесь все уезды по указанному городу!'
                                                '\nВыберите команду для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot, village, county):
    village = " ".join(map(str, village))
    counties = get_county('. ' + village, county)
    for i in counties:
        cur_county = call.data.strip()
        new_i = ''.join(map(str, i))
        new_i = new_i.strip()
        if cur_county in new_i:
            res = select_operation_get_counties(cur_county, '. ' + village)
            for church in res:
                reg_1 = generate_message(church)
                reg_1 = reg_1.replace('*', '')
                if len(reg_1) > 4096:
                    for x in range(0, len(reg_1), 4096):
                        bot.send_message(call.message.chat.id, reg_1[x:x + 4096], parse_mode='Markdown')
                        continue
                else:
                    bot.send_message(call.message.chat.id, reg_1, parse_mode='Markdown')
                    continue
    if call.data == 'Показать уезды заново':
        create_buttons_county(call, bot, village, county)
