from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def login() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Войти, как админ")
    kb.button(text="Войти, как пользователь")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
