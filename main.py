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
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
class ReferatOrder(StatesGroup):
    subject = State()
    topic = State()
    institution = State()
    pages = State()
    @dp.message_handler(lambda message: message.text == "📄 Referat")
async def referat_start(message: types.Message):
    await message.answer("Iltimos, fanni kiriting (masalan: Tarix, Informatika)")
    await ReferatOrder.subject.set()
    @dp.message_handler(state=ReferatOrder.subject)
async def referat_get_subject(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer("Endi referat mavzusini yozing.")
    await ReferatOrder.next()
    @dp.message_handler(state=ReferatOrder.topic)
async def referat_get_topic(message: types.Message, state: FSMContext):
    await state.update_data(topic=message.text)
    await message.answer("Qaysi ta’lim muassasasida o‘qiysiz?")
    await ReferatOrder.next()
    @dp.message_handler(state=ReferatOrder.institution)
async def referat_get_institution(message: types.Message, state: FSMContext):
    await state.update_data(institution=message.text)
    await message.answer("Nechta sahifalik referat kerak? (5-10, 20, 30-40)")
    await ReferatOrder.next()
    @dp.message_handler(state=ReferatOrder.pages)
async def referat_get_pages(message: types.Message, state: FSMContext):
    pages = message.text
    price = "3000 so'm"
    if "20" in pages:
        price = "5000 so'm"
    elif "30" in pages or "40" in pages:
        price = "10000 so'm"

    data = await state.get_data()
    await message.answer(
        f"Buyurtma qabul qilindi!\n\n"
        f"Fan: {data['subject']}\n"
        f"Mavzu: {data['topic']}\n"
        f"Ta’lim muassasasi: {data['institution']}\n"
        f"Sahifa: {pages}\n"
        f"Narx: {price}\n\n"
        f"Tez orada operator siz bilan bog‘lanadi yoki bot orqali to‘lov bo‘limi ishga tushadi."
    )
    await state.finish()
    
