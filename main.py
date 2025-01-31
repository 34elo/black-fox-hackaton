import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher

from handlers.login_handler import main_router




# Запуск бота
async def main():
    bot = Bot(token="")
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)

    # Ниже добавляем хендлеры
    dp.include_routers(main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
