from telebot import types


def handle_photo(bot, message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("удалить фотку", callback_data="delete")
    btn2 = types.InlineKeyboardButton("редактировать текст", callback_data="edit")

    markup.row(btn1, btn2)

    bot.reply_to(message, "классная фоточка", reply_markup=markup)