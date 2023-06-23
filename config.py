import logging
from aiogram import Bot, Dispatcher

API_Key = "6298564597:AAFxPkJyCIajSKrZHhg8Hm7lv4M2qzzwguY"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_Key)
dp = Dispatcher(bot)