import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Tokeningiz shu yerda
BOT_TOKEN = "7954657545:AAH3Wy7sGsxI_NyjOeZ-ZdK3kwN-ZAbpLdY"

# Bot va dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Menyu yaratamiz
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📄 Referat"),
    KeyboardButton("📊 Slayd"),
    KeyboardButton("✍️ Mustaqil ish"),
    KeyboardButton("📚 Kurs ishi"),
    KeyboardButton("💳 Balans"),
    KeyboardButton("⭐ Do'st taklif qilish"),
)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! Men AI Referat botman.",
        reply_markup=main_menu
    )

@dp.message_handler()
async def message_handler(message: types.Message):
    if message.text == "📄 Referat":
        await message.answer("Referat yozish bo'yicha buyurtma berish uchun mavzuni kiriting.")
    elif message.text == "📊 Slayd":
        await message.answer("Slayd tayyorlash uchun mavzuni yozing.")
    elif message.text == "✍️ Mustaqil ish":
        await message.answer("Mustaqil ish uchun mavzuni yozing.")
    elif message.text == "📚 Kurs ishi":
        await message.answer("Kurs ishi bo'yicha buyurtma berish uchun mavzuni kiriting.")
    elif message.text == "💳 Balans":
        await message.answer("Sizning balansingiz hozircha 0 so'm. To‘ldirish imkoniyati tez orada qo‘shiladi.")
    elif message.text == "⭐ Do'st taklif qilish":
        await message.answer("Do‘stingiz ushbu botga quyidagi havola orqali qo‘shilishi mumkin:\nhttps://t.me/AIreferatBot")
    else:
        await message.answer("Iltimos, menyudan birini tanlang.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
