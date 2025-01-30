from aiogram import Router, F
from aiogram.types import Message

router_admin_panel = Router()

def auto_schedule() -> None: # сформировать график
    pass

def send_notification() -> None: # отправка уведомелний сотрудникам о работе
    pass

def get_points() -> list[str]: # список таблиц с точками
    pass

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
    await message.answer('Выберите точку')


