from turtledemo.clock import make_hand_shape

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters.callback_data import CallbackQueryFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.utils.text_decorations import MarkdownDecoration

import keyboards.admin_keyboards
from db_work.admin.create_schedule import auto_schedule_create
from db_work.admin.edit_schedule import insert_to_schedule
from db_work.admin.format_text import format_worker_schedule_table
from db_work.admin.get_data_about_point import get_data_about_point
from db_work.admin.get_id_user import get_id_user
from db_work.admin.send_notifications import send_notifications
from db_work.admin.working_time import get_working_times
from keyboards import admin_keyboards
from keyboards.admin_keyboards import points_list, edit_schedule

router_admin_panel = Router()


class NotificationText(StatesGroup):
    text = State()


class ScheduleText(StatesGroup):
    worker = State()
    smena = State()
    points = State()


class Contact(StatesGroup):
    contact = State()


def get_points() -> list[str]:  # список таблиц с точками
    return ['25_Сентября_35а', '25_Сентября_35а/2', 'Багратиона_16', 'Дзержинского_9', 'Коммунистическая_6',
            'Лавочкина_54/6', 'Николаева_50', 'Ново-московская_2/8_ст4', 'Проспект_Гагарина_1/1', 'Рыленкова_18',
            'Энергетический_проезд3/4', 'Крупской_42']


@router_admin_panel.message(F.text == "Сформировать частичный график")
async def create_schedule(message: Message) -> None:
    auto_schedule_create('data/users_data.sqlite', 'data/schedule.sqlite')
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


@router_admin_panel.message(F.text == "Расписание на точках")
async def check_points(message: Message) -> None:
    text = 'Выберите точку из приведенных ниже\n\n'
    for item in get_points():
        text += ' - ' + item + '\n'
    await message.answer(text, reply_markup=points_list(get_points()))


@router_admin_panel.message(lambda message: message.text in get_points())
async def xyita(message: Message) -> None:
    ScheduleText.points = message.text
    table = f'Расписание {message.text}\n\n'
    datas = get_data_about_point(message.text)
    for i in datas.keys():

        if datas[i] != 'None':
            table += str(i) + ': ' + datas[i] + '\n'
        else:
            table += str(i) + ': ' + 'Не занято' + '\n'
    await message.answer(table)


@router_admin_panel.message(F.text == 'Меню')
async def main_menu(message: Message) -> None:
    await message.answer('Выберите действия', reply_markup=admin_keyboards.main())


@router_admin_panel.callback_query(F.data == 'Редактировать')
async def callback_query(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer(
        'Выберите день недели', keyboards = admin_keyboards.day_week())
    await state.set_state(ScheduleText.smena)


@router_admin_panel.message(ScheduleText.smena)
async def smena(message: Message, state: FSMContext) -> None:
    try:
        days_of_week = {
            "понедельник": "ПН",
            "вторник": "ВТ",
            "среда": "СР",
            "четверг": "ЧТ",
            "пятница": "ПТ",
            "суббота": "СБ",
            "воскресенье": "ВС"
        }
        m = str(message.text).lower().split(', ')
        res = days_of_week[m[0]]
        ScheduleText.smena = res
        await state.set_state(ScheduleText.worker)
        await message.answer('Напишите полное ФИО работника, которого вы хотите назначить на смену')
    except Exception as e:
        await message.answer('Ошибка, попробуйте снова')


@router_admin_panel.message(ScheduleText.worker)
async def worker(message: Message, state: FSMContext) -> None:
    try:
        ScheduleText.worker = message.text
        print(ScheduleText.worker, ScheduleText.smena, str(ScheduleText.points))
        insert_to_schedule(ScheduleText.points, ScheduleText.smena, ScheduleText.worker)
        await message.answer('График сформирован.Ознакомится с ним вы можете нажав на кнопку "Расписание на точках"')
        await state.clear()
    except Exception as e:
        print(e)
        await message.answer('Ошибка, попробуйте снова')


@router_admin_panel.message(F.text == 'Связаться с сотрудником')
async def contact(message: Message, state: FSMContext) -> None:
    await message.answer('Введите ФИО контакт, которого вам нужен')
    await state.set_state(Contact.contact)


@router_admin_panel.message(Contact.contact)
async def contact(message: Message, state: FSMContext) -> None:
    await message.answer(get_id_user(message.text))
    await state.clear()


@router_admin_panel.message(F.text == 'Количество смен у работников')
async def top_users(message: Message, state: FSMContext) -> None:
    text = 'Количество смен у работников\n\n'
    datas = get_working_times()
    for item in datas:
        text += str(item[0]) + ' - ' + str(item[1]) + '\n'
    await message.answer(text)


@router_admin_panel.message(F.text == 'Выгрузить в Excel')
async def excel(message: Message, state: FSMContext) -> None:
    await message.answer('В разработке')


@router_admin_panel.message(F.text == 'Загрузить из Excel')
async def excel(message: Message, state: FSMContext) -> None:
    await message.answer('В разработке')
