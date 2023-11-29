from aiogram import types
from aiogram.fsm.context import FSMContext

from apps.core.handlers import BaseHandler
from aiogram.exceptions import TelegramBadRequest

class StartHandler(BaseHandler):
    async def handle_all(self, state: FSMContext, **kwargs) -> None:
        await state.set_data({'count': (await state.get_data()).get('count', 0) + 1})
        await self.event.answer(f'Hi! {(await state.get_data()).get("count")}')
        await self.event.answer(f'Чтобы написать на другой акк в тг, напишите /open <id того, кому хотите написать>')

# Очевидно для тестирования здесь надо поменять значения на свои акки
user1 = {
    "id": 895958607,
    'username': 'fedorgugnin',
    'chats_with': -1
}
user2 = {
    'id': 6661514560,
    'username': 'fgug22',
    'chats_with': -1
}


class ForwardHandler(BaseHandler):
    async def handle_all(self, state: FSMContext, user) -> None:
        # chat_id - id конкретного пользователя в тг, а не id переписки, я долго с этим боролся -_-
        # тк self.event.text представляет из себя полный текст сообщения с командой, то нужно делать срез строки
        msg_text = self.event.text
        try:
            if user.id == user1['id']:
                if msg_text.startswith('/open'):
                    user1['chats_with'] = int(msg_text[len('/open') + 1:])
                    await self.event.answer(f'Вы теперь пишете { user2["username"] }\nЧтобы закрыть соединение, напишите /close')
                elif msg_text.startswith('/close'):
                    await self.event.answer('Соединение закрыто')
                    await self.bot.send_message(chat_id=user1['chats_with'], text="Соединение закрыто")
                    user2['chats_with'] = -1
                    user1['chats_with'] = -1
            if user.id == user2['id']:
                if msg_text.startswith('/open'):
                    user2['chats_with'] = int(msg_text[len('/open') + 1:])
                    await self.event.answer(
                        f'Вы теперь пишете {user1["username"]}\nЧтобы закрыть соединение, напишите /close')
                elif msg_text.startswith('/close'):
                    await self.event.answer('Соединение закрыто')
                    await self.bot.send_message(chat_id=user2['chats_with'], text="Соединение закрыто")
                    user2['chats_with'] = -1
                    user1['chats_with'] = -1
        except ValueError:
            await self.event.answer('Укажите id после /open!')

        try:
            if not msg_text.startswith('/'):
                if user.id == user1['id'] and user1['chats_with'] != -1:
                    user2['chats_with'] = user1['id']
                    await self.bot.send_message(chat_id=user1['chats_with'], text=msg_text)
                elif user.id == user2['id'] and user2['chats_with'] != -1:
                    user1['chats_with'] = user2['id']
                    await self.bot.send_message(chat_id=user2['chats_with'], text=msg_text)
        except TelegramBadRequest:
            await self.event.answer(f'Неверный id получателя или другая ошибка хз')

# class HelpHandler(BaseHandler):
#     async def handle_admin(self) -> None:
#         await self.event.answer('Помощь админу')
#
#     async def handle_worker(self) -> None:
#         await self.event.answer('Помощь психологу')
#
#     async def handle_user(self) -> None:
#         await self.event.answer('Помощь пользователю')
