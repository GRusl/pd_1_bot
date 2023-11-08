from aiogram.handlers import BaseHandler as BaseHandlerAiogram


class BaseHandler(BaseHandlerAiogram):
    async def handle(self) -> None:
        data = {
            'user': self.data['event_from_user'],
            'state': self.data['state']
        }

        user_id = self.data['event_from_user'].id

        """
        Логика распределения handle:
        Администратор может быть клиентом или психологом,
        но психолог не может быть клиентом
        """
        if user_id in [...]:  # Если пользователь администратор
            await self.handle_admin(**data)

        if user_id in [...]:  # Если пользователь психолог
            await self.handle_worker(**data)
        else:
            await self.handle_user(**data)  # handle для пользователей

        await self.handle_all(**data)  # handle для всех

    async def handle_all(self, **kwargs) -> None:
        pass

    async def handle_user(self, **kwargs) -> None:
        pass

    async def handle_admin(self, **kwargs) -> None:
        pass

    async def handle_worker(self, **kwargs) -> None:
        pass
