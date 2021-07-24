from aiogram.dispatcher.filters.state import StatesGroup, State


class Pay(StatesGroup):
    status_message = State()