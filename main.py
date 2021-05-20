import requests  # Імпорт бібліотеки requests
from datetime import datetime  # Імпорт дати та часу
import telebot  # Імпорт A Python implementation for the Telegram Bot API.
from auth_data import token  # Імпорт токена з BotFather


def telegram_bot():  # Функція виклику бота
    bot = telebot.TeleBot(token)  # Присвоєння змінній bot token з BotFather

    @bot.message_handler(commands=["start"])  # Дана функція відповідає користувачеві на команду /start
    def start_message(message):
        bot.send_message(message.chat.id,
                         "Welcome to telegram bot course work by Sprynskyi Oleksandr IK-31. If you want try me just send me one of this commands:"
                         "\n 'price' - to check current sell/buy BTC\n 'toss' - to toss a coinflip\n 'fact' - to get a random fact about number\n 'joke' - for cool or not joke\n 'player' - to see author steam stats")

    @bot.message_handler(content_types=["text"])  # Цей handler буде отримувати повідомлення користувача у форматі text та відправляти відповіді на команди
    def send_text(message):
        if message.text.lower() == "price":
            req = requests.get("https://yobit.net/api/2/btc_usd/ticker")  # Link до API
            response = req.json()  # Список у форматі JSON
            sell_price = response["ticker"]["sell"]  # Витягуєм ціну продажі з списку
            buy_price = response["ticker"]["buy"]   # Витягуєм ціну покупки з списку
            bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell BTC price: {sell_price},\nBuy BTC price: {buy_price}"
                    )  # Відправляєм повідомлення користувачені з актуальним курсом

        if message.text.lower() == "toss":
            url = "https://coin-flip1.p.rapidapi.com/headstails"  # Link з API

            headers = {
                    'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
                    'x-rapidapi-host': "coin-flip1.p.rapidapi.com"
                }  # Ключі за допомогою яких ми авторизовуємся в API

            response = requests.request("GET", url, headers=headers)
            answer = response.json()  # Список у форматі JSON
            coin_toss = answer["outcome"]  # Витягуєм результат робити з JSON
            bot.send_message(
                    message.chat.id,
                    f"{coin_toss}"
                )  # Відправляєм повідомлення користувачені з результатом роботи API

        if message.text.lower() == "fact":
            url = "https://numbersapi.p.rapidapi.com/random/trivia"  # Link з API

            querystring = {"json": "true", "fragment": "true", "max": "20", "min": "10"}  # Строка запиту яка являється частину унікального вказівника

            headers = {
                'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
                'x-rapidapi-host': "numbersapi.p.rapidapi.com"
            }  # Ключі за допомогою яких ми авторизовуємся в API

            response = requests.request("GET", url, headers=headers, params=querystring)  # Запит до API

            answer = response.json()  # Список у форматі JSON
            text = answer["text"]  # Витягуєм текст з JSON
            number = answer["number"]  # Витягуєм число з JSON
            type1 = answer["type"]  # Витягуєм тип факту з JSON

            bot.send_message(
                message.chat.id,
                f"Text: {text},\nNumber: {number},\nType:{type1}"
            )  # Відправляєм повідомлення користувачені з фактом про випадкове число

        if message.text.lower() == "joke":
            req = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")  # Link з API
            response = req.json()  # Список у форматі JSON
            category_joke = response["category"]  # Витягуєм категорію жарту з JSON
            tell_joke = response["joke"]  # Витягуєм жарт з JSON
            bot.send_message(
                message.chat.id,
                f"Category: {category_joke},\nJoke: {tell_joke}")  # Відповідаєм на повідомлення користувача

        if message.text.lower() == "player":
            req = requests.get("https://api.opendota.com/api/players/157417878")  # Link з API
            response = req.json()  # Список у форматі JSON
            rank_tier = response["rank_tier"]  # Витягуєм ранг автора
            profile_rank = response["solo_competitive_rank"]  # Витягуєм одиночні змагальні ігри
            profile_url = response["profile"]["profileurl"]  # Витягуєм профіль лінк
            profile_avatar = response["profile"]["avatar"]  # Витягуєм аватарку
            bot.send_message(
                message.chat.id,
                f"Author rank tier: {rank_tier}, \n Profile Rank: {profile_rank},\n Profile url: {profile_url}, \n Profile picture: {profile_avatar}")  # Відправляєм повідомлення користувачу
    bot.polling()


if __name__ == '__main__':
    telegram_bot()  # Викликаєм нашого бота
