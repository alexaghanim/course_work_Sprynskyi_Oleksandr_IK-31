import requests
from datetime import datetime
import telebot
from auth_data import token


def toss():
    url = "https://coin-flip1.p.rapidapi.com/headstails"

    headers = {
        'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
        'x-rapidapi-host': "coin-flip1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    answer = response.json()
    coin_toss = answer["outcome"]
    print(f"Outcome: {coin_toss}")


def get_data():
    req = requests.get("https://yobit.net/api/2/btc_usd/ticker")
    response = req.json()
    sell_price = response["ticker"]["sell"]
    buy_price = response["ticker"]["buy"]
    print(f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell BTC price: {sell_price},\nBuy BTC price: {buy_price}")


def joke():
    req = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
    response = req.json()
    category_joke = response["category"]
    tell_joke = response["joke"]
    print(f"Category: {category_joke},\nJoke: {tell_joke}")


def fact():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"json": "true", "fragment": "true", "max": "20", "min": "10"}

    headers = {
        'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
        'x-rapidapi-host': "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    answer = response.json()
    text = answer["text"]
    number = answer["number"]
    type1 = answer["type"]

    print(f"Text: {text},\nNumber: {number},\nType:{type1}")


def player():
    req = requests.get("https://api.opendota.com/api/players/157417878")
    response = req.json()
    rank_tier = response["rank_tier"]
    profile_rank = response["solo_competitive_rank"]
    profile_url = response["profile"]["profileurl"]
    profile_avatar = response["profile"]["avatar"]
    print(f"Author rank tier: {rank_tier}, \n Profile Rank: {profile_rank},\n Profile url: {profile_url}, \n Profile picture: {profile_avatar}")


def telegram_bot():
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id,
                         "Welcome to telegram bot course work by Sprynskyi Oleksandr IK-31. If you want try me just send me one of this commans:"
                         "\n 'price' - to check current sell/buy BTC\n 'toss' - to toss a coinflip\n 'fact' - to get a random fact about number\n 'joke' - for cool or not joke\n 'player' - to see author steam stats" )

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            req = requests.get("https://yobit.net/api/2/btc_usd/ticker")
            response = req.json()
            sell_price = response["ticker"]["sell"]
            buy_price = response["ticker"]["buy"]
            bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell BTC price: {sell_price},\nBuy BTC price: {buy_price}"
                    )

        if message.text.lower() == "toss":
            url = "https://coin-flip1.p.rapidapi.com/headstails"

            headers = {
                    'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
                    'x-rapidapi-host': "coin-flip1.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers)
            answer = response.json()
            coin_toss = answer["outcome"]
            bot.send_message(
                    message.chat.id,
                    f"{coin_toss}"
                )

        if message.text.lower() == "fact":
            url = "https://numbersapi.p.rapidapi.com/random/trivia"

            querystring = {"json": "true", "fragment": "true", "max": "20", "min": "10"}

            headers = {
                'x-rapidapi-key': "cfd5a271aamshd3c6c78cf253ddap1f8e31jsn62499f7674b1",
                'x-rapidapi-host': "numbersapi.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            answer = response.json()
            text = answer["text"]
            number = answer["number"]
            type1 = answer["type"]

            bot.send_message(
                message.chat.id,
                f"Text: {text},\nNumber: {number},\nType:{type1}"
            )

        if message.text.lower() == "joke":
            req = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
            response = req.json()
            category_joke = response["category"]
            tell_joke = response["joke"]
            bot.send_message(
                message.chat.id,
                f"Category: {category_joke},\nJoke: {tell_joke}")

        if message.text.lower() == "player":
            req = requests.get("https://api.opendota.com/api/players/157417878")
            response = req.json()
            rank_tier = response["rank_tier"]
            profile_rank = response["solo_competitive_rank"]
            profile_url = response["profile"]["profileurl"]
            profile_avatar = response["profile"]["avatar"]
            bot.send_message(
                message.chat.id,
                f"Author rank tier: {rank_tier}, \n Profile Rank: {profile_rank},\n Profile url: {profile_url}, \n Profile picture: {profile_avatar}")
    bot.polling()


if __name__ == '__main__':
    telegram_bot()
