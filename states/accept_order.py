from aiogram.dispatcher.filters.state import StatesGroup, State


class Order(StatesGroup):
    status_message = State()