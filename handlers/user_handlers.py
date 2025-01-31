from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_work.user.functions import get_all_points, get_free_shift, viev_schedule, get_name_from_username, \
    set_work_points, get_all_admins, get_all_schedule

router = Router()


@router.message(F.text == "Посмотреть свободные смены на определенной точке")
async def get_free_shift_message(message: Message):
    builder = InlineKeyboardBuilder()
    all_points = get_all_points()

    for i in all_points:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"get_free_shift_{i}"
        ))

    # Располагаем все кнопки вертикально (по одной в ряд)
    builder.adjust(2)

    await message.answer(
        'Выберите точку, у которой хотите посмотреть свободные смены',
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data[:15] == 'get_free_shift_')
async def send_free_shift(callback: CallbackQuery):
    point = callback.data[15:]
    m = get_free_shift(point)
    await callback.message.answer(f'{m}')


@router.message(F.text == "Посмотреть график в определенной точке")
async def get_schedule(message: Message):
    builder = InlineKeyboardBuilder()
    all_points = get_all_points()

    for i in all_points:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"get_schedule_{i}"
        ))

    # Располагаем все кнопки вертикально (по 2 в ряд)
    builder.adjust(2)

    await message.answer(
        'Выберите точку, у которой хотите посмотреть расписание',
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data[:13] == 'get_schedule_')
async def send_random_value(callback: CallbackQuery):
    point = callback.data[13:]
    # ФУНКЦИЯ КОТОРАЯ СОЗДАЕТ ГРАФИК
    await callback.message.answer(f'{str(point)}')


@router.message(F.text == "Посмотреть все свои смены")
async def handle_worker(message: Message):
    full_name = get_name_from_username(message.from_user.username)[0]
    print(full_name)
    text = viev_schedule(full_name)
    await message.answer(f"{text}")


@router.message(F.text == "Связь с администратором")
async def handle_worker_buttons(message: Message):
    builder = InlineKeyboardBuilder()
    all_admins = get_all_admins()[1]
    all_usernames = get_all_admins()[0]

    for i in range(len(all_admins)):
        builder.add(InlineKeyboardButton(
            text=all_admins[i],
            callback_data=f"ss_{all_usernames[i]}"
        ))

    # Располагаем все кнопки вертикально (по одной в ряд)
    builder.adjust(1)

    await message.answer(
        'Выберите Админа с которым хотите связаться',
        reply_markup=builder.as_markup()
    )

@router.callback_query(F.data[:3] == 'ss_' )
async def send_value(callback: CallbackQuery):
    print(get_all_admins()[0])
    await callback.message.answer(f'Вы можете связаться с этим админом по данному контакту:\n\n @{str(callback.data[3:])}')


@router.message(F.text == "Установить желаемые точки работы")
async def set_points(message: Message):
    builder = InlineKeyboardBuilder()
    all_points = get_all_points()

    for i in all_points:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"set_points_{i}"
        ))
    builder.add(InlineKeyboardButton(
        text='Закончить выбор точек',
        callback_data=f"set_points_break"
    ))
    # Располагаем все кнопки вертикально (по 2 в ряд)
    builder.adjust(2)

    await message.answer(
        'Выберите точки, у которых хотите посмотреть расписание',
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data[:11] == 'set_points_')
async def add_points(callback: CallbackQuery):
    point = callback.data[11:]
    username = callback.from_user.username
    set_work_points(username, point)
    await callback.message.answer(f'{str(point)} успешно добавлено в список ваших желаемых точек')


@router.message(F.text == "Установить желаемые смены")
async def go_set_work_schedule(message: Message):
    builder = InlineKeyboardBuilder()
    all_schedule = get_all_schedule()

    for i in all_schedule:
        builder.add(InlineKeyboardButton(
            text=i,
            callback_data=f"set_schedule_{i}"
        ))
    builder.add(InlineKeyboardButton(
        text='Закончить выбор смен',
        callback_data=f"set_schedule_break"
    ))
    # Располагаем все кнопки вертикально (по 2 в ряд)
    builder.adjust(2)

    await message.answer(
        'Выберите точки, у которых хотите посмотреть расписание',
        reply_markup=builder.as_markup()
    )
