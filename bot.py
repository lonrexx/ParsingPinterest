import asyncio
from aiogram import Bot, Dispatcher

from handlers import user_commands
from config import TOKEN

async def main():
    bot = Bot(TOKEN, parse_mode="HTML")
    dp = Dispatcher() 

    dp.include_router(
        user_commands.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())