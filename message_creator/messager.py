def message_creator(message, bot, call):
    """
    This function creates message by length of table
    :param message: message to change
    :return: message iterator
    """
    message_list = []
    ms = str()
    less_than_3480 = 0
    more_then_3480 = 3480
    splitted = message.splitlines(True)
    for mes in splitted:
        if less_than_3480 + len(mes) < more_then_3480:
            ms += mes
            less_than_3480 += len(mes)
        else:
            message_list.append(ms)
            ms = str()
            more_then_3480 += 3480
    else:
        message_list.append(ms)
    for message in message_list:
        bot.send_message(call.message.chat.id, message, parse_mode="Markdown")
