from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать график")
    kb.button(text="Отправить уведомления сотрудникам")
    kb.button(text="Посмотреть график на точках")
    kb.button(text="Сформировать график")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def points_list(arg: list[str]) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in arg:
        kb.button(text=str(i), callback_data=i)

    return kb.as_markup(resize_keyboard=True)