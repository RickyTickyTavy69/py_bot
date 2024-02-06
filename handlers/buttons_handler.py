from handlers.weather_handler import get_weather
from functions.load_games import load_games
from bot.bot import bot


def button_handler(message, text):
    if text == '🐈 погода':
        get_weather(message)
    elif text == "🐈 поиграть":
        load_games(message)
    elif text == "🐈 поговорить":
        bot.send_message(message.chat.id,
                         'конечно, ты можешь со мной поговорить, '
                         'мы котики всё понимаем, и можем помочь'
                         )
    elif text == "🐈 музыка":
        bot.send_message(message.chat.id, 'предлагаю вашему вниманию данную композицию')
