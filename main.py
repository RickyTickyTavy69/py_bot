
import random

from bot.bot import bot

from constants.miau import miau_variants
from handlers.photo_handler import handle_photo
from handlers.buttons_handler import button_handler

from handlers.callback_handler import handle_callback
from handlers.commands_handler import handle_command

from db.create_db import create_db, connect_db, close_connection, db_execute
from constants.buttons import buttons


@bot.message_handler(commands=["start", "help", "site", "website"])
def handle(message):
    print("Handling")
    handle_command(message)


@bot.message_handler()
def get_message(message):
    if message.text in buttons:
        button_handler(message, message.text)
    elif message.content_type == "photo":
        handle_photo(bot, message)
    else:
        if "не котик" in message.text.lower():
            bot.reply_to(message, "конечно, я котик! Hello Everynyan! How are you fine thank you!")
        elif "котик" in message.text.lower():
            bot.reply_to(message, "да, мы котики умные! Мы можем считать и писать! А ещё мы любим солёную рыбку")
        elif message.text == 'погода':
            bot.send_message(message.chat.id, 'погода по москве...')
        elif message.text == 'поиграть':
            bot.send_message(message.chat.id, 'давай поиграем...')
        elif message.text == 'поговорить':
            bot.send_message(message.chat.id,
                             'конечно, ты можешь со мной поговорить, '
                             'мы котики всё понимаем, и можем помочь'
                             )
        else:
            bot.reply_to(message, random.choice(miau_variants))


@bot.callback_query_handler(func=lambda callback: True)
def get_callback(callback):
    handle_callback(bot, callback)


# RUN
bot.infinity_polling()
