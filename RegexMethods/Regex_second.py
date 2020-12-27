from RegexMethods.Reg_first import reg_first, reg_second, reg_third, reg_fourth


def get_regex(res):
    str_ = " ".join(map(str, res))
    reg_1 = reg_first(str_)
    reg_1 = reg_second(reg_1)
    reg_1 = reg_third(reg_1)
    reg_1 = reg_fourth(reg_1)
    return reg_1
