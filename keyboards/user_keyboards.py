from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

worker_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать точку")],
        [KeyboardButton(text="Посмотреть график")],
        [KeyboardButton(text="Связь с начальством")]
    ],
    resize_keyboard=True
)