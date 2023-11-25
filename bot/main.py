import asyncio
import json
import os
import pathlib

import ffmpeg
import pandas as pd
import requests
import torch
import whisper
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import F
from aiogram import types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

voice_dir = "./voice"
models_dir = "./models"
video_dir = "./video"
excel_dir = "./"

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Loading model...")

model = whisper.load_model("small", device=device, download_root=models_dir)
print("Model loaded")

bot = Bot(token='6245856594:AAFYTsj17S0W6tbwnRrulxus_JwV5yfpWqc')

dp = Dispatcher()

print("Bot started")

builder = InlineKeyboardBuilder()
builder.add(types.InlineKeyboardButton(
    text="👍",
    callback_data="mock"),
    types.InlineKeyboardButton(
        text="👎",
        callback_data="mock")
)


@dp.callback_query(F.data == "mock")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Бот для принятия обращений")


@dp.message(Command("help"))
async def help(message: types.Message):
    await message.reply("Бот для принятия обращений")


@dp.message(Command("stats"))
async def help(message: types.Message):
    response = requests.get('http://localhost:8000/export_stats', json=[message.text])
    info = json.loads(response.text)
    await export_to_excel(info['theme_counts'], info['theme_group_counts'], info['executor_counts'], message)


def answer(message: types.Message, text):
    response = requests.post('http://0.0.0.0:8000/predict', json=[text])
    predictions = json.loads(response.text)
    print(predictions)

    if (len(predictions) == 0):
        return "Не понимаю обращение. Сформулируйте точнее."

    answer = ""
    for prediction in predictions:
        print(prediction)
        answer += f'Тематика: ' + prediction['theme'] + '\n'
        if prediction['theme_group']:
            answer += f'Группа тематик: ' + prediction['theme_group'] + '\n'
        if prediction['executor']:
            answer += f'Исполнитель: ' + prediction['executor']

        answer += '\n'
        return answer


@dp.message(F.text)
async def get_text(message: types.Message):
    await message.answer("Ваш запрос принят.")
    await message.answer(answer(message, message.text), reply_markup=builder.as_markup())


@dp.message(F.voice)
async def answer_voice(message: types.Message):
    voice_object = message.voice or message.audio
    pathlib.Path(voice_dir).mkdir(parents=True, exist_ok=True)
    filename = os.path.join(voice_dir, f"{voice_object.file_unique_id}")

    await bot.download(
        voice_object,
        destination=filename,
    )

    mess = await message.reply("Обработка аудио...")
    text = get_text(model, filename)
    await message.answer("Ваш запрос принят.")
    await mess.delete()
    ans = answer(message, text)
    if ans != "Не понимаю обращение. Сформулируйте точнее":
        await message.answer("Понял, Ваш запрос: " + text)
    await message.answer(ans, reply_markup=builder.as_markup())


@dp.message(F.video)
@dp.message(F.video_note)
async def answer_video(message: types.Message):
    pathlib.Path(video_dir).mkdir(parents=True, exist_ok=True)
    object = message.video or message.video_note or message.document

    filename = os.path.join(
        video_dir,
        f"{object.file_unique_id}",
    )

    await bot.download(
        object,
        destination=filename,
    )

    output_filename = filename

    mess = await message.reply("Обработка видео...")
    text = get_text(model, output_filename)
    await mess.delete()
    await message.reply(text)
    await message.answer("Ваш запрос принят.")
    ans = answer(message, text)
    if ans != "Не понимаю обращение. Сформулируйте точнее":
        await message.answer("Понял, Ваш запрос: " + text)
    await message.answer(ans, reply_markup=builder.as_markup())


def video_decoding(video_filename: str, ogg_audio_filename: str) -> None:
    try:
        ffmpeg.input(video_filename).output(
            ogg_audio_filename,
            format="ogg",
            acodec="libvorbis",
            ab="64k",
        ).overwrite_output().run()
    except Exception as E:
        raise E
        os.remove(ogg_audio_filename)
    finally:
        os.remove(video_filename)


def get_text(model, filename: str) -> str:
    try:
        result = model.transcribe(filename)
        return result["text"]
    except Exception as E:
        raise E
    finally:
        os.remove(filename)


async def export_to_excel(theme_counts, theme_group_counts, executor_counts, message: types.Message) -> None:
    theme_df = pd.DataFrame(
        theme_counts.items(),
        columns=['Тема', 'Количество обращений']
    ).reset_index(drop=True)
    await message.answer('<pre>' + theme_df.to_markdown() + '</pre>', parse_mode="html")
    theme_group_df = pd.DataFrame(
        theme_group_counts.items(),
        columns=['Группа тем', 'Количество обращений']
    ).reset_index(drop=True)
    await message.answer('<pre>' + theme_group_df.to_markdown() + '</pre>', parse_mode="html")
    executor_df = pd.DataFrame(
        executor_counts.items(),
        columns=['Исполнитель', 'Количество обращений']
    ).reset_index(drop=True)
    await message.answer('<pre>' + executor_df.to_markdown() + '</pre>', parse_mode="html")

    # with pd.ExcelWriter(os.path.join(excel_dir, 'path_to_file.xlsx')) as writer:
    # theme_df.to_excel(writer, sheet_name="Количество обращений по темам", index=False)
    # theme_group_df.to_excel(writer, sheet_name="Количество обращений по группам тем", index=False)
    # executor_df.to_excel(writer, sheet_name="Количество обращений по исполнителям", index=False)
    # await message.answer_document(executor_df)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
