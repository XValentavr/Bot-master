"""
Change information before show it to user
"""
import re


def reg_first(string: str) -> str:
    """
    delete new lines
    :param string: str
    :return: str
    """
    st = re.sub(r"\n|\r|\r\n", " ", string)
    return re.sub(r"\s{2,}", " ", st)


def reg_third(string: str) -> str:
    """
    changes ; to new line
    :param string: str
    :return: str
    """
    return re.sub(r";\s", "\n", string)


def reg_fourth(string: str) -> str:
    """
    markup needed data
    :param string: str
    :return: str
    """
    st = re.sub(r"народження:\s", "*народження:*\n", string)
    st = re.sub(r"шлюб:\s", "*шлюб:*\n", st)
    st = re.sub(r"смерть:\s", "*смерть:*\n", st)
    st = re.sub(r"сповідні відомості:\s", "*сповідні відомості:*\n", st)
    st = re.sub(r"\s–(\r\n|\r|\n|$)", "", st)
    st = re.sub(r";Дошлюбні Обшуки:\s", "\n*дошлюбні обшуки:*\n", st)
    return st
