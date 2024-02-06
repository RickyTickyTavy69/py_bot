from telebot import types

from constants.talk import talk_phrases
from handlers.weather_handler import get_weather


def handle_callback(bot, callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        # айдишки идут в возрастающем порядке, поэтому можно просто отнять единицу.
    elif callback.data == "edit":
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
    elif callback.data == "bad_mood":
        phrases = talk_phrases[1]
        message = phrases[0][0]
        markup = types.InlineKeyboardMarkup()
        button_yes = types.InlineKeyboardButton("Да", callback_data=f"phrases {phrases[0][1]}")
        button_no = types.InlineKeyboardButton("Нет", callback_data=f"phrases {phrases[0][2]}")
        markup.row(button_yes, button_no)
        bot.send_message(callback.message.chat.id, message, reply_markup=markup)
    elif "phrases" in callback.data:
        phrases = talk_phrases[1]
        idx = callback.data.split()[1]
        message = phrases[int(idx)][0]
        bot.send_message(callback.message.chat.id, message)
    elif callback.data == "музыка":
        message = 'хорошо, предлагаю вам послушать данную композицию'
