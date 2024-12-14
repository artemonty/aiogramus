import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from tokenfiles import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Онлайн-запись")],
        [KeyboardButton(text="Информация")],
        [KeyboardButton(text="Вопросы")],
    ],
    resize_keyboard=True
)

online_booking_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Записаться на стрижку")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)
info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О компании")],
        [KeyboardButton(text="Контакты")],
        [KeyboardButton(text="Назад")],
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Здравствуйте! Выберите нужное действие: ", reply_markup=main_menu_kb)

@dp.message(lambda message: message.text == "Онлайн-запись")
async def handle_online_booking(message: Message):
    await message.answer("Выберите действие:", reply_markup=online_booking_kb)

@dp.message(lambda message: message.text == "Информация")
async def handle_info(message: Message):
    await message.answer("Вот что я могу рассказать:", reply_markup=info_kb)

@dp.message(lambda message: message.text == "Назад")
async def handle_back(message: Message):
    await message.answer("Вы вернулись в главное меню. Выберите нужное действие:", reply_markup=main_menu_kb)

@dp.message(lambda message: message.text == "Записаться на стрижку")
async def handle_booking(message: Message):
    await message.answer("Отлично! Для записи напишите желаемую дату и время.")

@dp.message(lambda message: message.text == "Вопросы")
async def handle_questions(message: Message):
    await message.answer("Список частых вопросов и ответов: ...")

async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())