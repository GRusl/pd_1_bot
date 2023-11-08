from aiogram import types
from aiogram.fsm.context import FSMContext

from apps.core.handlers import BaseHandler


class StartHandler(BaseHandler):
    async def handle_all(self, state: FSMContext, **kwargs) -> None:
        await state.set_data({'count': (await state.get_data()).get('count', 0) + 1})
        await self.event.answer(f'Hi! {(await state.get_data()).get("count")}')


# class HelpHandler(BaseHandler):
#     async def handle_admin(self) -> None:
#         await self.event.answer('Помощь админу')
#
#     async def handle_worker(self) -> None:
#         await self.event.answer('Помощь психологу')
#
#     async def handle_user(self) -> None:
#         await self.event.answer('Помощь пользователю')

