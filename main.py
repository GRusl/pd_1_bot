import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from apps.main.routers import prepare_router as main_prepare_router
from db import init

TOKEN = getenv('BOT_TOKEN', '6988500207:AAFycbly-2ydY-0GAJ_5fC0YkDXRzyjkrgM')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)

    storage = RedisStorage.from_url(getenv('REDIS_URL', 'redis://127.0.0.1:6379'))
    await init()
    dp = Dispatcher(storage=storage)
    dp.include_router(main_prepare_router())

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
