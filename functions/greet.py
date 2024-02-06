from telebot import types
from bot.bot import bot

def greet(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('да, всё прекрасно <3', callback_data='good_mood'))
    markup.add(types.InlineKeyboardButton('чего то сегодня печалька...(', callback_data='bad_mood'))
    # keyboard

    reply_markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("🐈 погода")
    button2 = types.KeyboardButton("🐈 поиграть")
    button3 = types.KeyboardButton("🐈 поговорить")
    button4 = types.KeyboardButton("🐈 музыка")
    reply_markup.row(button, button2, button3, button4)

    photo = open('static/photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)  # method for sending a photo
    bot.send_message(message.chat.id,
                     f'<u><b>Приветик</b></u>, {message.from_user.first_name}! я - котик Марины \n Если ты Марина, я - твой котик! \n',
                     parse_mode="html",
                     reply_markup=reply_markup,
                     )
    bot.send_message(message.chat.id, ' Надеюсь, у тебя все отлично :)', reply_markup=markup)