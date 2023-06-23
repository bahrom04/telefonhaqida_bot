import logging
from aiogram import Bot, Dispatcher

API_Key = "TOKEN HERE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_Key)
dp = Dispatcher(bot)
