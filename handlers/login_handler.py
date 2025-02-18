from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db_work.login.already_auth import already_auth
from db_work.login.check_admin import check_admin_code
from db_work.login.check_user import check_worker_code
from db_work.login.put_chatID_schedule import put_data
from keyboards import login_keyboard, admin_keyboards, user_keyboards

main_router = Router()


class AuthAdmin(StatesGroup):
    admin_code = State()


class AuthWorker(StatesGroup):
    worker_code = State()


@main_router.message(CommandStart())
async def start(message: Message):
    if already_auth(message.chat.id)[0]:
        if already_auth(message.chat.id)[1]:
            await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
        else:
            await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
    else:
        await message.answer('Вы не авторизованы', reply_markup=login_keyboard.main())


@main_router.message(F.text == 'Войти, как сотрудник')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите код сотрудника")
    await state.set_state(AuthWorker.worker_code)


@main_router.message(F.text == 'Войти, как руководитель')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите код руководителя")
    await state.set_state(AuthAdmin.admin_code)


@main_router.message(AuthWorker.worker_code)
async def message_with_text(message: Message, state: FSMContext):
    if check_worker_code(message.text):
        await state.clear()
        await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
        await put_data(message.from_user.id, 'Сотрудник')
    else:
        await message.answer('Данные неверны, Попробуйте снова')
        await state.set_state(AuthWorker.worker_code)


@main_router.message(AuthAdmin.admin_code)
async def message_with_text(message: Message, state: FSMContext):
    if check_admin_code(message.text):
        await state.clear()
        await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
        await put_data(message.from_user.id, 'Администратор')

    else:
        await message.answer('Данные неверны, Попробуйте снова')
        await state.set_state(AuthAdmin.admin_code)
