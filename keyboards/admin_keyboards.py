from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Сформировать график")
    kb.button(text="Отправить уведомления сотрудникам")
    kb.button(text="Посмотреть график на точках")
    kb.button(text="Сформировать график")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def points_list(arg: list[str]) -> ReplyKeyboardMarkup:
    for i in arg:
        buttons = [
            [
                types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
                types.InlineKeyboardButton(text="+1", callback_data="num_incr")
            ],
            [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return