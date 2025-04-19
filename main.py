from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(msg: Message):
    await msg.answer("Salom! AI Referat botga xush kelibsiz.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
