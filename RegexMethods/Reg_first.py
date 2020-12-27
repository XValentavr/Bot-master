import re


def reg_first(str):
    st = re.sub(r"\n|\r|\r\n", ";", str)
    return st


def reg_second(str):
    st = re.sub(r"\s\;", " ", str)
    return st


def reg_third(str):
    st = re.sub(r";\s(?![^(]*\))", "\n", str)
    return st


def reg_fourth(str):
    st = re.sub(r"Сумський державний архів\s", "Сумський державний архів:\n", str)
    st = re.sub(r"народження:\s", "*народження:*\n", st)
    st = re.sub(r"шлюб:\s", "*шлюб:*\n", st)
    st = re.sub(r"смерть:\s", "*смерть:*\n", st)
    st = re.sub(r"сповідні відомості:\s", "*сповідні відомості:*\n", st)
    st = re.sub(r"\s–(\r\n|\r|\n|$)", "", st)
    st = re.sub(r";Дошлюбні Обшуки:\s", "\n*дошлюбні обшуки:*\n", st)
    return st
