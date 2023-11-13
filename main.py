import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from apps.main.routers import prepare_router as main_prepare_router

TOKEN = getenv('BOT_TOKEN')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)

    storage = RedisStorage.from_url(getenv('REDIS_URL'))

    dp = Dispatcher(storage=storage)
    dp.include_router(main_prepare_router())

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())