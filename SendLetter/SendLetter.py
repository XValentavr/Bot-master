"""
This module send message if command is selected
"""


def to_order(message, bot) -> None:
    """
    send message when /order cpmmand is selected
    :param message: message
    :param bot: telebot
    :return: None
    """
    bot.send_message(message.chat.id,
                     'За дополнительной информацией обращайтесь к @Valentavr\n'
                     'Или отправьте письмо на почтовый ящик **iwilly17@gmail.com**',
                     parse_mode='Markdown')
