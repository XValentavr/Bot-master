from MySQLCommand.SelectChurches import get_Churches
import re
from RegexMethods.Regex_second import generate_message
from MySQLCommand.MySQLSelect import SelectOperation
from Sorted import SortedBy

global_cities = list()
CURRENT_CITY = [None]
global_region = []
current_region = ""


def visualization(message, bot, user_dict_mysql):
    chat_id = message.chat.id
    user = user_dict_mysql[chat_id]
    user.village = message.text
    mtrcs = [None for i in range(3)]
    words = user.village.split()
    last_village_g = ''
    province = ''
    if len(words) == 3:
        mtrcs[0] = words[0]
        mtrcs[1] = words[1]
        mtrcs[2] = words[2]
    elif len(words) == 2:
        mtrcs[0] = words[0]
        mtrcs[1] = None
        mtrcs[2] = words[1]
        text = ''.join(map(str, words[1]))
        strin = 'кого'

        result = re.findall(r'кого\w*', text)

        if strin == ''.join(map(str, result)):
            mtrcs[1] = None
            mtrcs[2] = words[1]
        else:
            mtrcs[2] = None
            mtrcs[1] = words[1]
    else:
        mtrcs[0] = words[0]
        mtrcs[1] = ''

    if mtrcs[1] == None and mtrcs[2] == None:
        first_village = mtrcs[0]
        province = ' '
        last_village_g = '. ' + first_village

    if mtrcs[1] == None and mtrcs[0] is not None and mtrcs[2] is not None:
        first_village = mtrcs[0]
        province = mtrcs[2]
        last_village_g = '. ' + first_village

    if mtrcs[2] == None and mtrcs[0] is not None and mtrcs[1] is not None:
        first_village = mtrcs[0]
        second_village = mtrcs[1]
        province_ = ' '
        last_village_g = '. ' + first_village + ' ' + second_village
        province = province_

    if mtrcs[0] is not None and mtrcs[1] is not None and mtrcs[2] is not None:
        village = mtrcs[0]
        second_village = mtrcs[2]
        province_ = ' '
        last_village_g = '. ' + village + ' ' + second_village
        province = province_
    if mtrcs[1] == None:
        mtrcs[1] = ''
    CURRENT_CITY[0] = (''.join(map(str, mtrcs[0] + ' ' + mtrcs[1])))
    global global_cities
    _, count = get_Churches(last_village_g.rstrip(), ' ')
    global_cities = [None for _ in range(count)]
    if count == 0:
        bot.send_message(message.chat.id, ' Извините, ничего не найдено.\nПроверьте данные')
    if count >= 5:
        churches, counter = get_Churches(last_village_g.rstrip(), ' ')
        counter -= 1
        for church in churches:
            global_cities[counter] = church
            counter -= 1
        new_c = counter
        final_global_cities = [None for _ in range(len(global_cities))]
        for i in global_cities:
            new_church = str(i)
            while (len(new_church.encode('utf-8'))) > 64:
                new_church = new_church.split()
                new_church.pop()
                new_church = ' '.join(map(str, new_church))
            final_global_cities[new_c] = new_church.strip()
            new_c -= 1
        global_cities = final_global_cities
        global current_region
        if mtrcs[2] != None:
            current_region = mtrcs[2]
        else:
            current_region = ' '
        SortedBy.sorted_by(bot, message)
    else:
        res = SelectOperation(last_village_g, province)
        for i in res:
            reg_1 = generate_message(i)
            if len(reg_1) > 4096:
                for x in range(0, len(reg_1), 4096):
                    bot.send_message(message.chat.id, reg_1[x:x + 4096], parse_mode='Markdown')
            else:
                bot.send_message(message.chat.id, reg_1, parse_mode='Markdown')
