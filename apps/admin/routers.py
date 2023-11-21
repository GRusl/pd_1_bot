from aiogram import Router
from aiogram.filters import Command

from apps.admin.handlers import AddAdminHandler, AddWorkerHandler, ProcessInputHandler
from apps.admin.states import UserInput


def prepare_router() -> Router:
    router = Router()

    router.message.register(AddAdminHandler, Command('add_admin'))
    router.message.register(AddWorkerHandler, Command('add_worker'))
    router.message.register(ProcessInputHandler, UserInput.user_id)

    return router
