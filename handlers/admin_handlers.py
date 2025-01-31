import io

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InputFile

from keyboards.admin_keyboards import points_list

router_admin_panel = Router()


def get_data_about_point() -> {}:
    schedule = {
        "Понедельник": {
            "Утро": "Иван",
            "Вечер": "Анна",
        },
        "Вторник": {
            "Утро": "Мария",
            "Вечер": "Петр",
        },
        "Среда": {
            "Утро": "Иван",
            "Вечер": "Анна",
        },
        "Четверг": {
            "Утро": "Мария",
            "Вечер": "Петр",
        },
        "Пятница": {
            "Утро": "Иван",
            "Вечер": "Анна",
        },
        "Суббота": {
            "Утро": "Мария",
            "Вечер": "Петр",
        },
        "Воскресенье": {
            "Утро": "Иван",
            "Вечер": "Анна",
        },
    }
    return schedule


def format_schedule_table(schedule, shop_name):
    """Форматирует расписание в виде таблицы."""

    # Определение максимальной длины для выравнивания
    max_day_len = max(len(day) for day in schedule)
    max_name_len = max(max(len(name) for name in shifts.values()) for shifts in schedule.values())

    header = f"| {'День':<{max_day_len}} | {'Утро':<{max_name_len}} | {'Вечер':<{max_name_len}} |\n"
    separator = f"|{'-' * (max_day_len + 2)}|{'-' * (max_name_len + 2)}|{'-' * (max_name_len + 2)}|\n"

    table = header + separator
    for day, shifts in schedule.items():
        morning_shift = shifts.get("Утро", " - ")
        evening_shift = shifts.get("Вечер", " - ")
        table += f"| {day:<{max_day_len}} | {morning_shift:<{max_name_len}} | {evening_shift:<{max_name_len}} |\n"

    formatted_text = f"<b>График работы магазина: {shop_name}</b>\n<pre>{table}</pre>"
    return formatted_text  # <pre> чтобы форматирование выглядело таблицей


def auto_schedule() -> None:  # сформировать график
    pass


def send_notification() -> None:  # отправка уведомелний сотрудникам о работе
    pass


def get_point_info(arg) -> None:  # Запрос в бд на получение инфы о точке
    pass


def get_points() -> list[str]:  # список таблиц с точками
    return ['Дзержинка', 'Гагарина']


@router_admin_panel.message(F.text == "Сформировать график")
async def create_schedule(message: Message):
    auto_schedule()
    await message.answer('График сформирован')


@router_admin_panel.message(F.text == "Отправить уведомления сотрудникам")
async def send_notification_tg(message: Message):
    send_notification()


@router_admin_panel.message(F.text == "Графики на точках")
async def check_points(message: Message):
    await message.answer('Выберите точку', reply_markup=points_list(get_points()))


@router_admin_panel.callback_query(F.data)
async def callback_on(callback: CallbackQuery):
    formatted_table = format_schedule_table(get_data_about_point(), callback.data)
    await callback.message.answer(formatted_table, parse_mode=ParseMode.HTML)
