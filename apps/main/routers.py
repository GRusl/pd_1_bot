from aiogram import Router
from aiogram.filters import CommandStart, Command

from apps.main.handlers import StartHandler, ForwardHandler


def prepare_router() -> Router:
    router = Router()

    router.message.register(StartHandler, CommandStart())
    router.message.register(ForwardHandler)
    return router
