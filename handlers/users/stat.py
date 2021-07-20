from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from datetime import datetime

from keyboards.inline.main_keyboard import diapason_statistic, cancel
from utils.db_api.order_controller import get_orders_by_date, get_all_orders, get_order_by_diapason
from utils.format_message import format_counter_message
from utils.stat_action import get_week_dict, get_month_dict
from loader import dp


@dp.callback_query_handler(text_contains='stat', state='*')
async def stat_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f'Выбери диапазон для просмотра:')
    await call.message.edit_reply_markup(reply_markup=await diapason_statistic())


async def get_message(call, order_list, title):
    if len(order_list) >= 1:
        values = await create_values(order_list)
        send_message = await format_counter_message(title, values)
        await call.message.edit_text(send_message)
        await call.message.edit_reply_markup(reply_markup=await cancel())
    else:
        call.message.edit_text('Нету статистики за выбранный промежуток времени')
        call.message.edit_reply_markup(reply_markup=await cancel())


async def create_values(order_list):
    values_dict = {}
    counter = 0
    for order in order_list:
        counter += order.amount_spend
    values_dict['count'] = len(order_list)
    values_dict['amount'] = counter
    return values_dict


@dp.callback_query_handler(text_contains='day', state='*')
async def stat_day(call: CallbackQuery, state: FSMContext):
    await state.finish()
    orders = await get_orders_by_date(datetime.today())
    await get_message(call, orders, 'Статистика за день:')


@dp.callback_query_handler(text_contains='week', state='*')
async def stat_month(call: CallbackQuery, state: FSMContext):
    await state.finish()
    date_dict = get_week_dict()
    orders = await get_order_by_diapason(date_dict['date_from'], date_dict['date_to'])
    await get_message(call, orders, 'Статистика за неделю:')


@dp.callback_query_handler(text_contains='month', state='*')
async def stat_month(call: CallbackQuery, state: FSMContext):
    await state.finish()
    date_dict = get_month_dict()
    orders = await get_order_by_diapason(date_dict['date_from'], date_dict['date_to'])
    await get_message(call, orders, 'Статистика за месяц:')


@dp.callback_query_handler(text_contains='all_time', state='*')
async def stat_month(call: CallbackQuery, state: FSMContext):
    await state.finish()
    date_dict = get_month_dict()
    orders = await get_order_by_diapason(date_dict['date_from'], date_dict['date_to'])
    await get_message(call, orders, 'Статистика за все время:')




