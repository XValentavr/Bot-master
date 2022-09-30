def message_creator(message, bot, call):
    """
    This function creates message by length of table
    :param message: message to change
    :return: message iterator
    """
    message_list = []
    ms = str()
    less_than_3250 = 0
    more_then_3250 = 3250
    splitted = message.splitlines(True)
    for mes in splitted:
        if less_than_3250 + len(mes) < more_then_3250:
            ms += mes
            less_than_3250 += len(mes)
        else:
            ms += mes
            message_list.append(ms)
            ms = str()
            more_then_3250 += 3250
    else:
        message_list.append(ms)
    for message in message_list:
        try:
            bot.send_message(call.message.chat.id, message, parse_mode="Markdown")
        except AttributeError:
            bot.send_message(call.chat.id, message, parse_mode="Markdown")
