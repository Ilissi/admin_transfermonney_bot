from aiogram.dispatcher.filters.state import StatesGroup, State


class Ticker(StatesGroup):
    ticker = State()
