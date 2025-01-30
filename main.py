import asyncio
from handlers import user_handlers, admin_handlers
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(user_handlers.router, admin_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
