from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery

from keyboards.admin_keyboards import points_list

router_admin_panel = Router()

def auto_schedule() -> None: # сформировать график
    pass

def send_notification() -> None: # отправка уведомелний сотрудникам о работе
    pass

def get_point_info(arg) -> None: # Запрос в бд на получение инфы о точке
    pass

def get_points() -> list[str]: # список таблиц с точками
    return['Дзержика', 'Гагарина']

@router_admin_panel.message(F.text == "Сформировать график")
async def create_schedule(message: Message):
    auto_schedule()
    await message.answer('График сформирован')


@router_admin_panel.message(F.text == "Отправить уведомления сотрудникам")
async def create_schedule(message: Message):
    send_notification()
    await message.answer('Уведомления отправлены всем сотрудникам')


@router_admin_panel.message(F.text == "Посмотреть график на точках")
async def create_schedule(message: Message):
    await message.answer('Выберите точку', reply_markup=points_list(get_points()))

@router_admin_panel.callback_query(F.data)
async def point_info(callback: CallbackQuery):
    await callback.message.answer(callback.data)