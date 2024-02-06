from bot.bot import bot


def print_help(message):
    bot.send_message(message.chat.id,
                     '<u><b>Привет</b></u> Я котик Марины Д. из Москоу. Да, мы котики умные, даже в телеге есть. Мы '
                     'можем поговорить или поиграть',
                     parse_mode="html")
