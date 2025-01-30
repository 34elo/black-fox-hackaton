from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="функция 1")
    kb.button(text="функция 2")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

