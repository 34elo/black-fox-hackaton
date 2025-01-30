from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Администратор"), KeyboardButton(text="Работник")]
    ],
    resize_keyboard=True
)