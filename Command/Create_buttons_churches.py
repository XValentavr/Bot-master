from telebot import types
from MySQLCommand.Select_from_information_about_churches import SelectOperation
from RegexMethods.Regex_second import generate_message


def create_buttons_churches(message, bot, cities):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in cities:
        key = types.InlineKeyboardButton(text=i, callback_data=i)
        keyboard.add(key)
    key = types.InlineKeyboardButton(text='Показать церкви заново', callback_data='Показать церкви заново')
    keyboard.add(key)
    bot.send_message(message.from_user.id, text='Здесь все церкви по указанному городу!'
                                                '\nВыберите команду для большей информации ',
                     reply_markup=keyboard)


def callback_worker(call, bot, cities, current_churches, current_region):
    cur_churches = " ".join(map(str, current_churches))
    for i in cities:
        new_data = call.data.strip()
        new_i = ''.join(map(str, i))
        new_i = new_i.strip()
        if new_data in new_i:
            res = SelectOperation(new_data, '. ' + cur_churches, current_region)
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
    if call.data == 'Показать церкви заново':
        create_buttons_churches(call, bot, cities)
