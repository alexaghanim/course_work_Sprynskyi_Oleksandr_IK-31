import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/2/btc_usd/ticker")
    response = req.json()
    sell_price = response["ticker"]["sell"]
    buy_price = response["ticker"]["buy"]
    print(f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell BTC price: {sell_price},\nBuy BTC price: {buy_price}")


def telegram_bot():
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Welcome to telegram bot course work by Sprynskyi Oleksandr IK-31. If you want try me just send me one of this messages:\n 'price' - to check current sell/buy BTC")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/2/btc_usd/ticker")
                response = req.json()
                sell_price = response["ticker"]["sell"]
                buy_price = response["ticker"]["buy"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M')}\nSell BTC price: {sell_price},\nBuy BTC price: {buy_price}"
                )
            except Exception as ex:
                print(ex)
        else:
            bot.send_message(message.chat.id, "What i don't understand you!")
    bot.polling()


if __name__ == '__main__':
    telegram_bot()
