from aiogram import types
from aiogram.fsm.context import FSMContext

from apps.core.handlers import BaseHandler
from apps.admin.states import UserInput


class AddAdminHandler(BaseHandler):
    async def handle_admin(self, state: FSMContext, **kwargs) -> None:
        await self.event.answer('Введите ID пользователя:')
        await state.set_state(UserInput.user_id)


class AddWorkerHandler(BaseHandler):
    async def handle_admin(self, state: FSMContext, **kwargs) -> None:
        await self.event.answer('Введите ID пользователя::')
        await state.set_state(UserInput.user_id)


class ProcessInputHandler(BaseHandler):
    async def handle_admin(self, state: FSMContext, message: types.Message, **kwargs) -> None:
        user_input = message.text
        response = f'Вы ввели: {user_input}, все прошло успешно!'
        await self.event.answer(response)
        await state.clear()
