from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Войти, как руководитель")
    kb.button(text="Войти, как сотрудник")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
