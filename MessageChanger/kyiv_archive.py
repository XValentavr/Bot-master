import re

from MessageChanger.check_and_change import checker_date
from MessageChanger.not_kyiv_archive import del_special_character


def kyiv(data):
    fund = analizer([kyiv_reg_to_get_data(d.lower(), "fund") for d in data if d != ""])
    description = analizer([kyiv_reg_to_get_data(d.lower(), 'description') for d in data if d != ""])
    case = [kyiv_reg_to_get_data(d.lower(), 'case') for d in data if d != ""]
    year = [kyiv_reg_to_get_data(d.lower(), 'year') for d in data if d != '']
    year, fund, description, case = delete_nones(year, fund, description, case)
    return checker_date(year=year, description=description, fund=fund, case=case)


def kyiv_reg_to_get_data(data: str, where: str):
    """
    Regex to get information
    :param data: data to check
    :param where: flag to set where show info
    :return: result of regex
    """
    if where == "fund":
        fund = re.search(r"(?<=фонд ).*?(?=, оп)", data, flags=re.DOTALL)
        if fund is not None:
            return del_special_character(fund, None)
        else:
            return None
    if where == 'description':
        description = re.search(r"(?<=опис ).*?(?=, cпра)", data, flags=re.DOTALL)
        if description is None:
            description = re.search(r"(?<=опис ).*?(?=, спра)", data, flags=re.DOTALL)
        if description is not None:
            return del_special_character(description, None)
        else:
            return None
    if where == 'year':
        year = re.search(r"(?<=\().*?(?=\))", data, flags=re.DOTALL)
        if year is not None:
            return re.sub(r"[^0-9,–-]+", "", year.group(0)).strip()
        else:
            return None
    if where == 'case':
        data = modify_case(data)
        if data is not None:
            case = re.search(r"(?<=^).*?(?=$)", data, flags=re.DOTALL)
            if case is not None:
                return del_special_character(case, 'case')
            else:
                return None
        else:
            return None


def analizer(list_to_a: list):
    """
    This function changes list
    :param list_to_a: list to change
    :return: changed list
    """
    number = None
    for index, value in enumerate(list_to_a):
        if value is not None:
            number = value
        else:
            list_to_a[index] = number
    return list_to_a


def modify_case(data: str):
    """
    This function deletes unused parameters from str
    :param data: string to modify
    :return: new modified string
    """
    symbols = []
    if '(' in data:
        res = data.split('(')[0]
        if ',' in res:
            for i, s in enumerate(res):
                if s == ',':
                    symbols.append(i)
            res = res[symbols[-1]:]
            res = check_digits(res.split(',')[1])
            return res
        return check_digits(res.strip())
    return None


def check_digits(data: str):
    count = 0
    for d in data:
        if d.isdigit():
            count += 1
    if count >= 1:
        return data
    else:
        return None


def delete_nones(year, fund, description, case):
    new_year = []
    new_fund = []
    new_description = []
    new_case = []
    for i, v in enumerate(year):
        if v is not None:
            if v != '':
                new_year.append('|' + v + '|')
                new_fund.append(fund[i])
                new_case.append(case[i])
                new_description.append(description[i])
    return new_year, new_fund, new_description, new_case
