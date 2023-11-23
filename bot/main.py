import json

import telebot
import requests
from pydantic import TypeAdapter

from api.app.data_models.prediction import Prediction

bot = telebot.TeleBot('token')

typeAdapter = TypeAdapter(list[Prediction])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Задай вопрос")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Бот для хакатона]")
    else:
        response = requests.post('/predict', json = {"texts": [message]})
        predictions = typeAdapter.validate_python(json.loads(response.text))
        answer = ""
        for prediction in predictions:
            answer += f'Тема: {prediction.theme}\n'
            if prediction.theme_group:
                answer += f'Группа тем: {prediction.theme_group}\n'
            if prediction.executor:
                answer += f'Исполнитель: {prediction.executor}'

            answer += '\n'


        bot.send_message(message.from_user.id, answer)



if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)