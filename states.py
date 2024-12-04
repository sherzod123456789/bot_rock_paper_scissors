from aiogram.dispatcher.filters.state import State, StatesGroup


class Wait(StatesGroup):
    game = State()