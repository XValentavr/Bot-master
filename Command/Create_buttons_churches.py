from telebot import types
from MySQLCommand.Select_from_information_about_churches import select_operation_get_churches
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


def callback_worker(call, bot, cities, current_churches, cur_region):
    cur_locality = " ".join(map(str, current_churches))
    for i in cities:
        cur_church = call.data.strip()
        new_i = ''.join(map(str, i))
        new_i = new_i.strip()
        if cur_church in new_i:
            res = select_operation_get_churches(cur_church, '. ' + cur_locality, cur_region)
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
