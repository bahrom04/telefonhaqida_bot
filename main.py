from aiogram import executor
from config import dp
from Data_base import user
from handlers import handlers

async def on_startup(_):
    print('Bot is online')
    user.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)