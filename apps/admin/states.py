from aiogram.fsm.state import StatesGroup
from aiogram.fsm.state import State


class UserInput(StatesGroup):
    user_id = State()
