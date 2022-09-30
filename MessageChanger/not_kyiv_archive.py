import re


def not_kyiv(datalist: list):
    """
    This function works with metrics not in Kyiv archive
    :param datalist: list of metrics
    :return: table string
    """
    year = [re_to_get_data(data.lower(), "year") for data in datalist if data != ""]
    fund = [re_to_get_data(data.lower(), "fund") for data in datalist if data != ""]
    description = [
        re_to_get_data(data.lower(), "description") for data in datalist if data != ""
    ]
    case = [re_to_get_data(data.lower(), "case") for data in datalist if data != ""]

    return year, fund, description, case


def re_to_get_data(data: str, where: str):
    """
    Regex to get information
    :param data: data to check
    :param where: flag to set where show info
    :return: result of regex
    """
    if where == "case":
        case = re.search(r"(?<=спр.).*?(?=$)", data, flags=re.DOTALL)
        if case is not None:
            return del_special_character(case,'case')
        else:
            return None
    elif where == "description":
        description = re.search(r"(?<=оп.).*?(?=спр.)", data, flags=re.DOTALL)
        if description is not None:
            return del_special_character(description,None)
        else:
            return None
    elif where == "fund":
        fund = re.search(r"(?<=ф.).*?(?=оп.)", data, flags=re.DOTALL)
        if fund is not None:
            return del_special_character(fund,None)
        else:
            return None
    elif where == "year":
        year = re.search(r"(?<=^).*?(?=ф)", data, flags=re.DOTALL)
        if year is not None:
            res = re.sub(r"[;:]", "", year.group(0).strip())
            if res != "":
                return f"|{res}|"
            else:
                return ""
        return None


def del_special_character(data,flag):
    if flag =='case':
        res = re.sub(r"\W+,", "", data.group(0)).strip()
    else:
        res = re.sub(r"\W+", "", data.group(0)).strip()

    return f"{res}"
