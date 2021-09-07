"""from telebot import types
from MySQLCommand.Select_from_information_about_churches import SelectOperation
from RegexMethods.Regex_second import generate_message

city = []
final_city = []
cur_region = ''


def create_buttons_new_churches(message, bot, cities, current_region):
    keyboard = types.InlineKeyboardMarkup()
    global final_city
    global cur_region
    cur_region = current_region
    final_city = [None for _ in range(len(cities))]
    count = 0
    if len(final_city) != 0:
        for i in cities:
            if i is not None:
                city.append(i)
                for ct in city:
                    if ct not in final_city:
                        final_city[count] = ct
                key = types.InlineKeyboardButton(text=ct, callback_data=ct)
                keyboard.add(key)
            count += 1
        key = types.InlineKeyboardButton(text='Показать церкви заново', callback_data='Показать церкви заново')
        keyboard.add(key)
        bot.send_message(message.from_user.id, text='Здесь все церкви по указанному городу!'
                                                    '\nВыберите команду для большей информации ',
                         reply_markup=keyboard)


def callback_worker(call, bot, current_churches):
    cur_churches = " ".join(map(str, current_churches))
    global cur_region
    cur_ = cur_region
    new_data = call.data.strip()
    for i in final_city:
        new_i = ''.join(map(str, i)).strip()
        if new_data == new_i:
            res = SelectOperation(new_data, '. ' + cur_churches, cur_)
            for i in res:
                reg_1 = generate_message(i)
                if len(reg_1) > 4096:
                    for x in range(0, len(reg_1), 4096):
                        bot.send_message(call.message.chat.id, reg_1[x:x + 4096], parse_mode='Markdown')
                        continue
                else:
                    bot.send_message(call.message.chat.id, reg_1, parse_mode='Markdown')
                    continue
    if call.data == 'Показать церкви заново':
        create_buttons_new_churches(call, bot, final_city, cur_region)
"""