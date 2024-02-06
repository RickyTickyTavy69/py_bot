import json
import requests

from bot.bot import bot

from functions.greet import greet


def get_weather(message, state="moscow"):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid=f4f6a1617c20a0f3102039d0e1d52df4&units=metric")
    # response = f"{res.json()}"
    data = json.loads(res.text)

    temp = data['main']['temp']
    img = "cat_winter.gif" if temp < -2 else "cat_summer.gif"
    file = open(f"static/{img}", "rb")
    bot.send_animation(message.chat.id, file)

    bot.reply_to(message, f" погода в городе {state}: \n"
                          f"температура: {temp} °C \nощущается как {data['main']['feels_like']} ")
    bot.send_message(message.chat.id, "чтобы узнать погоду в другом городе - введите название города")
    bot.send_message(message.chat.id, "Чтобы вернуться назад - наберите exit")
    bot.register_next_step_handler(message, get_weather_city)


def get_weather_city(message):
    if message.text.lower() != "exit":
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=f4f6a1617c20a0f3102039d0e1d52df4&units=metric")
        data = json.loads(res.text)
        if data['cod'] != 200:
            bot.reply_to(message, f"к сожаленью, ваш город не найден. Вы ввели {message.text}")
        else:
            temp = data['main']['temp']
            img = "cat_winter.gif" if temp < -2 else "cat_summer.gif"
            file = open(f"static/{img}", "rb")
            bot.send_animation(message.chat.id, file)

            bot.reply_to(message, f" погода в городе {message.text}: \n"
                              f"температура: {data['main']['temp']} °C \nощущается как {data['main']['feels_like']} ")
        bot.send_message(message.chat.id, "чтобы узнать погоду в другом городе - введите название города")
        bot.send_message(message.chat.id, "Чтобы вернуться назад - наберите exit")
        bot.register_next_step_handler(message, get_weather_city)
    else:
        greet(message)
