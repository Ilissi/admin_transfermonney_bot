from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

import typing

from utils.callback import pay_cb
from utils.db_api.transaction_conroller import update_transaction, get_transaction
from states.accept_pay import Pay
from loader import dp, bot_admin


@dp.callback_query_handler(pay_cb.filter(accept='True'), state='*')
async def accept_order(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.finish()
    transaction = await get_transaction(int(callback_data['pay_id']))
    if transaction.status == 'Не подтверждена':
        await update_transaction(transaction.id, 'Подтверждена')
        await bot_admin.send_message(transaction.user_id, 'Пополнение ID {}\n<b>Подтверждено</b>'.format(transaction.id))
        await call.message.answer('Действие подтверждено')
    else:
        await call.message.answer('Действие подтверждено ранее')


@dp.callback_query_handler(pay_cb.filter(accept='False'), state="*")
async def remove_order(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.finish()
    transaction = await get_transaction(int(callback_data['pay_id']))
    if transaction.status == 'Не подтверждена':
        await Pay.status_message.set()
        await state.update_data(transaction_id=transaction.id)
        await call.message.answer('Напиши причину отказа платежа:')
    else:
        await call.message.answer('Действие подтверждено ранее')


@dp.message_handler(state=Pay.status_message)
async def remove_message(message: Message, state: FSMContext):
    ticker_data = await state.get_data()
    await state.finish()
    await update_transaction(int(ticker_data['transaction_id']), message.text)
    transaction = await get_transaction(int(ticker_data['transaction_id']))
    await bot_admin.send_message(transaction.user_id, 'Пополнение ID {}\n<b>Отклонено</b>'.format(transaction.id))
    await message.answer('Действие подтверждено')

