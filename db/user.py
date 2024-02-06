# потом доделать

def register_user(bot, message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    name = username if (len(username) != 0) else first_name + last_name

    if len(name) == 0:
      name = ask_name(bot, message)




def ask_name(bot, message):
    bot.send_message(message.chat.id, "назовите ваше имя, пожалуйста")
