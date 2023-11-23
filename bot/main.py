import json

import telebot
import requests

bot = telebot.TeleBot('token')




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Задай вопрос")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Бот для хакатона]")
    else:
        response = requests.post('api', json = {"question": f'{message.text}'})
        bot.send_message(message.from_user.id, json.loads(response.text))



if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)