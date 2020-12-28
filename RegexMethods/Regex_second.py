import re


def generate_message(res):
    res = remove_new_lines(res)
    return res[0] + '\n' \
           + res[1] + '\n' \
           + format_birth(res[2]) \
           + format_wedding(res[3]) \
           + format_divorce(res[4]) \
           + format_death(res[5]) \
           + format_testament(res[6]) \
           + format_additional(res[7])


def remove_new_lines(res):
    new_res = []
    for r in res:
        new_r = re.sub(r"\n|\r|\r\n", " ", r)
        new_r = re.sub(r"\s{2,}", " ", new_r)
        new_res.append(new_r)
    return new_res


def format_birth(birth):
    if is_empty(birth):
        return ''
    birth = replace_semicolon_to_newline(birth)
    return re.sub(r"^\s?народження:\s?(.*)$", r"*народження:*\n\1", birth, flags=re.DOTALL) + '\n'


def format_wedding(wedding):
    if is_empty(wedding):
        return ''
    wedding = replace_semicolon_to_newline(wedding)
    return re.sub(r"^\s?шлюб:\s?(.*)$", r"*шлюб:*\n\1", wedding, flags=re.DOTALL) + '\n'


def format_divorce(divorce):
    if is_empty(divorce):
        return ''
    divorce = replace_semicolon_to_newline(divorce)
    return divorce + '\n'


def format_death(death):
    if is_empty(death):
        return ''
    death = replace_semicolon_to_newline(death)
    return re.sub(r"^\s?смерть:\s?(.*)$", r"*смерть:*\n\1", death, flags=re.DOTALL) + '\n'


def format_testament(testament):
    if is_empty(testament):
        return ''
    testament = replace_semicolon_to_newline(testament)
    return testament + '\n'


def format_additional(additional):
    if is_empty(additional):
        return ''
    additional = replace_semicolon_to_newline(additional)
    return additional + '\n'


def is_empty(string):
    return re.search(r"^\s*[-–]\s*$", string)


def replace_semicolon_to_newline(string):
    return re.sub(r";\s?", "\n", string)
