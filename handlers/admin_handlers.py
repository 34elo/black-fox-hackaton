from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from db_work.admin.create_schedule import auto_schedule_create
from db_work.admin.format_text import format_schedule_table
from db_work.admin.get_data_about_point import get_data_about_point
from db_work.admin.send_notifications import send_notifications
from keyboards import admin_keyboards
from keyboards.admin_keyboards import points_list

router_admin_panel = Router()


class NotificationText(StatesGroup):
    text = State()


def get_points() -> list[str]:  # список таблиц с точками
    return ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
            'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
            'Энергетический_проезд3/4', 'Крупской_42']


@router_admin_panel.message(F.text == "Сформировать частичный график")
async def create_schedule(message: Message) -> None:
    auto_schedule_create()
    await message.answer('График сформирован')


@router_admin_panel.message(F.text == "Отправить уведомления сотрудникам")
async def send_notification_tg(message: Message, state: FSMContext) -> None:
    await message.answer('Напишите ваше сообщение-рассылку')
    await state.set_state(NotificationText.text)


@router_admin_panel.message(NotificationText.text)
async def message_with_text(message: Message, state: FSMContext) -> None:
    send_notifications(message.text)
    await message.answer('Ваше уведомление сотрудникам отправлено')
    await state.clear()


@router_admin_panel.message(F.text == "Графики на точках")
async def check_points(message: Message) -> None:
    text = ''
    await message.answer(f'Выберите точку из приведенных ниже {get_points()}', reply_markup=points_list(get_points()))


@router_admin_panel.message(lambda message: message.text in get_points())
async def xyita(message: Message) -> None:
    formatted_table = format_schedule_table(get_data_about_point(message.text), message.text)
    await message.answer(formatted_table, parse_mode=ParseMode.HTML)


@router_admin_panel.message(F.text == 'Меню')
async def main_menu(message: Message) -> None:
    await message.answer('Выберите действия', reply_markup=admin_keyboards.main())
