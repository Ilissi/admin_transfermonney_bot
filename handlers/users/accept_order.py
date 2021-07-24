from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

import typing

from utils.callback import order_cb
from utils.db_api.order_controller import get_orders, update_order
from utils.db_api.user_controller import get_user_id, update_user_balance_set
from states.accept_order import Order
from loader import dp, bot_admin


@dp.callback_query_handler(order_cb.filter(accept='True'), state="*")
async def accept_order(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.finish()
    ticker = await get_orders(int(callback_data['order_id']))
    if ticker.accepted is False:
        await update_order(ticker.id, 'Оплата подтверждена', True)
        await bot_admin.send_message(ticker.user_id, 'Заказ ID {}\n<b>Подтвержден</b>'.format(ticker.id))
        await call.message.answer('Действие подтверждено')
    elif ticker.accepted is True:
        await call.message.answer('Действие подтверждено ранее')


@dp.callback_query_handler(order_cb.filter(accept='False'), state="*")
async def remove_order(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.finish()
    ticker = await get_orders(int(callback_data['order_id']))
    if ticker.accepted is False:
        await Order.status_message.set()
        await state.update_data(ticker_id=ticker.id)
        await call.message.answer('Напиши причину отказа платежа:')
    elif ticker.accepted is True:
        await call.message.answer('Действие подтверждено ранее')


@dp.message_handler(state=Order.status_message)
async def remove_message(message: Message, state: FSMContext):
    ticker_data = await state.get_data()
    await state.finish()
    await update_order(int(ticker_data['ticker_id']), message.text, True)
    ticker = await get_orders(int(ticker_data['ticker_id']))
    user = await get_user_id(ticker.user_id)
    new_balance = round(user.balance + ticker.amount_spend, 2)
    await update_user_balance_set(ticker.user_id, new_balance)
    await bot_admin.send_message(ticker.user_id, 'Пополнение ID {}\n<b>Отклонено</b>'.format(ticker.id))
    await message.answer('Действие подтверждено')

