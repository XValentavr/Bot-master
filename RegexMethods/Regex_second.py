import re


def generate_message(res):
    res = list(res)
    count = 0
    for i in res:
        if i == None:
            res[count] = ' '
        count += 1
    return res[0] + '\n' \
           + res[1] + '\n' \
           + format_birth(res[2]) \
           + format_wedding(res[3]) \
           + format_divorce(res[4]) \
           + format_death(res[5]) \
           + format_testament(res[6]) \
           + format_additional(res[7])


def remove_new_lines(res):
    if res != None:
        new_res = []
        for r in res:
            new_r = re.sub(r"\s{2,}", " ", r)
            new_res.append(new_r)
        return new_res


def remove_forbidden_characters(res):
    if res != None:
        new_res = []
        for r in res:
            new_r = re.sub(r"[`*]", " ", r)
            new_res.append(new_r)
        return new_res


def format_birth(birth):
    if birth != None:
        birth = replace_semicolon_to_newline(birth)
        return re.sub(r"^\s?народження:\s?(.*)$", r"*народження:*`\n\1`", birth, flags=re.DOTALL) + '\n'


def format_wedding(wedding):
    if wedding != None:
        wedding = replace_semicolon_to_newline(wedding)
        return re.sub(r"^\s?шлюб:\s?(.*)$", r"*шлюб:*`\n\1`", wedding, flags=re.DOTALL) + '\n'


def format_divorce(divorce):
    if divorce != None:
        divorce = replace_semicolon_to_newline(divorce)
        return divorce + '\n'


def format_death(death):
    if death != None:
        death = replace_semicolon_to_newline(death)
        return re.sub(r"^\s?смерть:\s?(.*)$", r"*смерть:*`\n\1`", death, flags=re.DOTALL) + '\n'


def format_testament(testament):
    if testament != None:
        testament = replace_semicolon_to_newline(testament)
        return re.sub(r"^\s?сповідні відомості:\s?(.*)$", r"*сповідні відомості:*`\n\1`", testament,
                      flags=re.DOTALL) + '\n'


def format_additional(additional):
    if additional != None:
        additional = replace_semicolon_to_newline(additional)
        return additional + '\n'


def replace_semicolon_to_newline(string):
    if string != None:
        return string.replace(';', '\n')
