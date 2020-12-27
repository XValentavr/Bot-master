from MySQLCommand.SelectChurches import get_Churches
from ChatVizualization import On_chat
from Command import Create_buttons_regions
import re
from Command.Create_buttons_churches import create_buttons_churches
from Command.Create_buttons_regions import create_buttons_regions
from Command import Create_buttons_regions
from RegexMethods.Regex_second import get_regex
from MySQLCommand.RegionGetter import get_Region
from MySQLCommand.MySQLSelect import SelectOperation
from MySQLCommand.ChurchesCounter import get_Churches_counter

global_cities = []
global_cities_second = []
CURRENT_CITY = [None for i in range(1)]
global_region = []


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
    region = get_Region(last_village_g)
    local_region = []
    CURRENT_CITY[0] = (''.join(map(str, mtrcs[0] + ' ' + mtrcs[1])))
    for reg in region:
        new_region = " ".join(map(str, reg))
        string = new_region.split()
        if len(string) >= 7:
            if string[6] == 'пов.':
                local_region.append(string[5])
        if len(string) >= 6:
            if string[5] == 'пов.':
                local_region.append(string[4])
        if len(string) >= 8:
            if string[7] == 'пов.':
                local_region.append(string[6] )
    sorted_region = []
    for i in local_region:
        if i not in sorted_region:
            sorted_region.append(i)

    global global_region
    global_region = [None for i in range(len(sorted_region))]
    c = 0
    global global_cities
    for i in sorted_region:
        global_region[c] = sorted_region[c]
        c += 1
    if len(global_region) > 1:
        create_buttons_regions(message, bot, global_region, CURRENT_CITY)
    else:
        count = get_Churches_counter(last_village_g, ' ')
        global_cities = [None for i in range(count)]
        c = count - 1
        if count == 0:
            bot.send_message(message.chat.id, ' Извините, ничего не найдено.\nПроверьте данные')
        if count >= 5:
            churches = get_Churches(last_village_g, ' ')
            for church in churches:
                zero = church[0].split()
                if zero[0] == 'церква':
                    new_church = " ".join(map(str, church))
                    new_church = re.sub('\(.*', '', new_church, flags=re.DOTALL)
                    new_church = re.sub(',.*', '', new_church, flags=re.DOTALL)
                    new_church = re.sub('.' + mtrcs[0] + '.*', '', new_church, flags=re.DOTALL)
                else:
                    new_church = " ".join(map(str, church))
                    new_church = re.sub('церква.*', '', new_church, flags=re.DOTALL)
                    new_church = re.sub('.' + mtrcs[0] + '.*', '', new_church, flags=re.DOTALL)
                if (len(new_church.encode('utf-8'))) > 64:
                    new_i = ''.join(map(str, new_church)).split()[:-1]
                    new_i.pop(0)
                    global_cities[c] = ' '.join(map(str, new_i))
                elif (new_church[-1] == '.'):
                    global_cities[c] = (new_church + ' ' + mtrcs[0])
                else:
                    if zero[0] != 'церква':
                        if (len(new_church.encode('utf-8'))) < 51:
                            new_church = new_church + 'церква'
                    global_cities[c] = new_church
                c -= 1
            create_buttons_churches(message, bot, global_cities)

        else:
            res = SelectOperation(last_village_g, province)
            for i in res:
                reg_1 = get_regex(i)
                if len(reg_1) > 4096:
                    for x in range(0, len(reg_1), 4096):
                        bot.send_message(message.chat.id, reg_1[x:x + 4096], parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, reg_1, parse_mode='Markdown')
