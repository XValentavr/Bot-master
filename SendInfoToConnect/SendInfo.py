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
    bot.send_message(
        message.chat.id,
        "За дополнительной информацией обращайтесь к @Valentavr\n\n"
        "Или отправьте письмо на почтовый ящик iwilly17@gmail.com\n\n"
        "Связаться с нами в <a href='https://www.facebook.com/groups/502963204384298'>Facebook</a>"
        "Или непосредственно заполнить форму, используя команду /form",
        parse_mode="HTML",
        disable_web_page_preview=True,
    )
