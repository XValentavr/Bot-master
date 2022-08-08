from FormCRM.RegistrationUser import Mono

bot_value = Mono()


def init_feedback(bot, message):
    """
    This module starts feadback
    :param bot: bot API
    :param message: bot chat info
    :return: None
    """

    bot_value.bot = bot
    bot_value.bot.send_message(
        message.chat.id, "Введіть Ваш коментар. (Для виходу напишіть exit)"
    )
    bot_value.bot.register_next_step_handler(message, register_feadback)


def register_feadback(message):
    feadback = message.text
    if feadback == "exit" or feadback == "Exit":

        from Command import ForStartMenu

        ForStartMenu.some_action(message, bot_value.bot)

    else:
        bot_value.bot.send_message(
            message.chat.id, "Дякуємо за коментар!")

        bot_value.bot.send_message(
            469236353,
            feadback)
