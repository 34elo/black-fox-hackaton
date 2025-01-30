from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать частичный график")
    kb.button(text="Отправить уведомления сотрудникам")
    kb.button(text="Посмотреть график на точку")
    kb.button(text="")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def points_list(arg: list[str]) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in arg:
        kb.button(text=i, callback_data=i)
        print(i)

    return kb.as_markup(resize_keyboard=True)