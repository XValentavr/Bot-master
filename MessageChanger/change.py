import re
from math import floor


def changer(message: dict) -> str:
    return table_blueprint(message.get('archive'), message.get('village'), message.get('county'),
                           message.get('province'), message.get('church'), message.get('birth'))


def table_blueprint(archive, village, county, province, church, birth) -> str:
    '''
    This module creates table blueprint
    :return: blueprint of table
    '''
    max_length = lambda string: len(string)
    p_lambda = lambda prvnc: prvnc.split(',')[0].strip()

    maxer = max_length(f'Назва повіту і губернії - {county.strip()}, {p_lambda(province.strip())}')
    dots = ''.join([' ' for _ in range(maxer)])
    last_td = td = ''.join([' ' for _ in range(round(maxer / 4) - 2)])
    if ((maxer / 4) - 2) - len(td) == 0.5 or ((maxer / 4) - 2) - len(td) == 0.25:
        last_td = td + ' '
    elif ((maxer / 4) - 2) == len(td):
        last_td = last_td[:len(last_td) - 1]

    metrics_changer(birth, archive)
    table = f"|{check_and_add(f'Назва архіву - {archive.strip()}', maxer)}\n" \
            f"|{check_and_add(f'Назва села - {village.strip()}', maxer)}\n" \
            f"|{check_and_add(f'Назва повіту і губернії - {county.strip()}, {p_lambda(province.strip())}', maxer)}\n" \
            f"|{check_and_add(f'Назва церкви - {church.strip()}', maxer)}\n" \
            f"|{dots}|\n" \
            f"|{check_and_add(metric_title(birth) if metric_title(birth) else None, maxer)}\n" \
            f"|Фонд|{td}|Опис|{td}|Справа|{last_td}|Рік|"
    return table


def check_and_add(string, max_string):
    """
    This function create special string to create table
    :param string: string to upgrade
    :param max_string: length of string to add symbols
    :return: new updated string
    """
    # if string is empty then return
    if string is None:
        return None

    # else add data
    difference = floor((max_string - len(string)) / 2)
    if difference % 2 != 0 or (difference % 2 == 0 and difference < (max_string - len(string)) / 2):
        difference += 1
    for _ in range(difference):
        string = ' ' + string
        string += ' '
    if len(string) > max_string:
        string = string[:len(string) - (len(string) - max_string)]
    return string + '|'


def metric_title(metric: str) -> str | None:
    """
    This function gets metric title
    :param metric:  metric to get title
    :return: title
    """
    if metric is not None:
        return metric.split('\n')[0].replace('*', '')
    return None


def metrics_changer(metric: str, archive: str) -> str | None:
    """
    This module change metric string to table
    :param metric: string to change
    :return:  new string to enter into table
    """
    if metric is None:
        return None
    if 'історичний архів в м. Київ' not in archive:
        data = metric.split('\n')
        del data[0]
        for i, d in enumerate(data):
            if data[i] == '' or data[i] == ' ':
                del data[i]
        not_kyiv(data)
    else:
        pass


def not_kyiv(datalist: list) -> str:
    """
    This function works with metrics not in Kyiv archive
    :param datalist: list of metrics
    :return: table string
    """
    year = []
    fund = []
    description = []
    case = []
    for data in datalist:
        if data != '':
            pass
