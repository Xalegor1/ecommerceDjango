import os
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6172964755:AAGcrmdT_96pVQ_w92IdO-3nrnY1Lr-NyRY")
dp = Dispatcher(bot)

BASE_URL = "http://localhost:8000/api"


def get_products():
    url = f"{BASE_URL}/items_api/"
    response = requests.get(url)
    products = response.json()
    return products


markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton('Каталог товаров'))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выбери, что тебе нужно:", reply_markup=markup)


@dp.message_handler(Text(equals='Каталог товаров'))
async def send_catalog(message: types.Message):
    # получаем список товаров
    products = get_products()
    os.makedirs("tmp", exist_ok=True)
    count = 0
    for product in products:
        title = product.get("title")
        price = product.get("price")
        image_url = product.get("image")
        image_response = requests.get(image_url)
        image_file = f"tmp/{title}.jpg"
        with open(image_file, "wb") as f:
            f.write(image_response.content)
        with open(image_file, "rb") as f:
            await bot.send_photo(message.chat.id, f, caption=f"<b>Название Товара: {title}</b>\nЦена: {price}$", parse_mode=ParseMode.HTML)
        os.remove(image_file)
        count += 1
    await message.answer(f"Всего {count} товаров")    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
