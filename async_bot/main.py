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


# создаем функцию для получения товаров с API магазина
def get_products():
    url = f"{BASE_URL}/items_api/"
    response = requests.get(url)
    products = response.json()
    return products


# Создаем клавиатуру с двумя кнопками "Привет" и "Пока"
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(KeyboardButton("Привет"), KeyboardButton("Пока"), KeyboardButton('Каталог товаров'))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Отправляем приветственное сообщение и клавиатуру с двумя кнопками
    """
    await message.answer("Привет! Я бот, который умеет здороваться. Выбери, что тебе нужно:", reply_markup=markup)


@dp.message_handler(Text(equals="Привет"))
async def say_hello(message: types.Message):
    """
    Отправляем сообщение "Привет" в ответ на нажатие кнопки "Привет"
    """
    await message.answer("Привет!")


@dp.message_handler(Text(equals="Пока"))
async def say_goodbye(message: types.Message):
    """
    Отправляем сообщение "Пока" в ответ на нажатие кнопки "Пока"
    """
    await message.answer("Пока!")

@dp.message_handler(Text(equals='Каталог товаров'))
async def send_catalog(message: types.Message):
    # получаем список товаров
    products = get_products()
    # создаем временную директорию для хранения изображений
    os.makedirs("tmp", exist_ok=True)
    # формируем сообщение с каталогом товаров
    for product in products:
        title = product.get("title")
        price = product.get("price")
        image_url = product.get("image")
        image_response = requests.get(image_url)
        # сохраняем изображение во временный файл
        image_file = f"tmp/{title}.jpg"
        with open(image_file, "wb") as f:
            f.write(image_response.content)
        # отправляем сообщение с названием товара, ценой и изображением
        with open(image_file, "rb") as f:
            await bot.send_photo(message.chat.id, f, caption=f"<b>Название Товара: {title}</b>\nЦена: {price}$", parse_mode=ParseMode.HTML)
        # удаляем временный файл
        os.remove(image_file)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
