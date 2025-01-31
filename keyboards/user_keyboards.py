from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Посмотреть свободные смены на определенной точке")],
            [KeyboardButton(text="Посмотреть график в определенной точке")],
            [KeyboardButton(text="Посмотреть все свои смены")],
            [KeyboardButton(text="Связь с администратором")],
            [KeyboardButton(text="Установить желаемые точки работы")],
            [KeyboardButton(text="Установить желаемые смены")]
        ],
        resize_keyboard=True
    )
