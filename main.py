import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers.admin_handlers import router_admin_panel
from handlers.login_handler import main_router
from handlers.user_handlers import router


# Запуск бота
async def main():
    bot = Bot(token="7970347344:AAGhbs_C2DoGZpFOJ_ywDEwUbjzFS3WajVs")
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)

    # Ниже добавляем хендлеры
    dp.include_routers(main_router, router_admin_panel, router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
