from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


router = Router()
TOKEN = '7170658393:AAG8fbrrzkIFMR59b7lRIHqJLHEZa9z6Xvg'

# Клавиатура для выбора роли
role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Администратор"), KeyboardButton(text="Работник")]
    ],
    resize_keyboard=True
)

# Клавиатура для работника
worker_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать точку")],
        [KeyboardButton(text="Посмотреть график")],
        [KeyboardButton(text="Связь с начальством")]
    ],
    resize_keyboard=True
)


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Кто ты, воин?", reply_markup=role_keyboard)


@router.message(lambda message: message.text == "Работник")
async def worker_menu(message: types.Message):
    await message.answer("Меню работника:", reply_markup=worker_keyboard)


@router.message(lambda message: message.text in ["Выбрать точку", "Посмотреть график", "Связь с начальством"])
async def handle_worker_buttons(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}")


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
