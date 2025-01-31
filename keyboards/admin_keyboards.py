from aiogram.types import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardMarkup


def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать частичный график")
    kb.button(text="Отправить уведомления сотрудникам")
    kb.button(text="Графики на точках")
    kb.button(text="")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def points_list(arg: list[str]) -> InlineKeyboardMarkup:
    buttons = [
        [],
    ]
    for item in arg:
        buttons[0].append(InlineKeyboardButton(text=item, callback_data=item))
        print(item)

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
