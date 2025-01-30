from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards import login_keyboard, admin_keyboards, user_keyboards

main_router = Router()


class AuthAdmin(StatesGroup):
    admin_code = State()


class AuthWorker(StatesGroup):
    worker_code = State()


def check_admin_code(arg) -> bool:  # проверка на админа в бд
    pass


def check_worker_code(arg) -> bool:  # проверка на сотрудника в бд
    pass


def already_auth(chat_id) -> (bool, bool):  # уже зареган(true) / админ или сотрудник(false)
    return True, True


@main_router.message(CommandStart())
async def start(message: Message):
    # await message.answer_sticker(sticker="")
    if already_auth(message.chat.id)[0]:
        if already_auth(message.chat.id)[1]:
            await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
        else:
            await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
    else:
        await message.answer('Вы не авторизованы',reply_markup=user_keyboards.main())


@main_router.message(F.text == 'Войти, как сотрудник')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите код сотрудника")
    await state.set_state(AuthWorker.worker_code)


@main_router.message(F.text == 'Войти, как руководитель')
async def message_with_text(message: Message, state: FSMContext):
    await message.answer("Введите код руководителя")
    await state.set_state(AuthAdmin.admin_code)


@main_router.message(AuthWorker.worker_code)
async def message_with_text(message: Message):
    if check_worker_code(message.text):
        await message.answer('Вы успешно авторизовались', reply_markup=user_keyboards.main())
    # кидает в табличку с пользователями и их ролями


@main_router.message(AuthAdmin.admin_code)
async def message_with_text(message: Message):
    if check_admin_code(message.text):
        await message.answer('Вы успешно авторизовались', reply_markup=admin_keyboards.main())
    # кидает в табличку с пользователями и их ролями
