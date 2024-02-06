import config

from telebot import types
from bot.bot import bot


def load_games(message):
    web_app = types.WebAppInfo(url=f"{config.website_url}")
    web_app_results = types.WebAppInfo(url=f"{config.website_url}/results")
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("старт", web_app=web_app)
    markup.add(button)

    reply_markup = types.ReplyKeyboardMarkup()
    game_button = types.KeyboardButton("начать игру", web_app=web_app)
    results_button = types.KeyboardButton("посмотреть результаты", web_app=web_app_results)
    reply_markup.row(game_button, results_button)

    bot.send_message(message.chat.id, 'давай поиграем...', reply_markup=reply_markup)
    bot.send_message(message.chat.id, '<3', reply_markup=markup)
