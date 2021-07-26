from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext


from keyboards.inline.main_keyboard import search_menu, cancel
from states.search_ticker import Ticker
from states.search_user import User
from utils.format_message import show_message, user_message
from utils.db_api.order_controller import get_orders
from utils.db_api.user_controller import get_user
from loader import dp, bot


@dp.callback_query_handler(text_contains='search', state='*')
async def stat_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('Поиск статистики')
    await call.message.edit_reply_markup(reply_markup=await search_menu())


@dp.callback_query_handler(text_contains='ticker', state='*')
async def stat_user(call: CallbackQuery, state: FSMContext):
    await Ticker.ticker.set()
    await call.message.edit_text('Введите id тикера:')
    await call.message.edit_reply_markup()


@dp.message_handler(state=Ticker.ticker)
async def search_ticker(message: Message, state: FSMContext):
    await state.finish()
    ticker_id = int(message.text)
    ticker = await get_orders(ticker_id)
    if ticker:
        await bot.send_message(message.chat.id, text=show_message(ticker), reply_markup=await cancel())
    else:
        await message.answer('Тикер не найден!', reply_markup=await cancel())


@dp.callback_query_handler(text_contains='user', state='*')
async def stat_user(call: CallbackQuery, state: FSMContext):
    await User.username.set()
    await call.message.edit_text('Введите username пользователя:')
    await call.message.edit_reply_markup()


@dp.message_handler(state=User.username)
async def search_user(message: Message, state: FSMContext):
    await state.finish()
    username = message.text
    user = await get_user(username)
    if user:
        await bot.send_message(message.chat.id, text=user_message(user), reply_markup=await cancel())
    elif user is None:
        await message.answer('Пользователь не найден!', reply_markup=await cancel())


