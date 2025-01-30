from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from keyboards.user_keyboards import worker_keyboard
from keyboards.role_keyboard import role_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Кто ты, воин?", reply_markup=role_keyboard)


@router.message(lambda message: message.text == "Работник")
async def worker_menu(message: types.Message):
    await message.answer("Меню работника:", reply_markup=worker_keyboard)


@router.message(lambda message: message.text in ["Выбрать точку", "Посмотреть график", "Связь с начальством"])
async def handle_worker_buttons(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}")
