from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from states.add_balance import Balance
from utils.format_message import update_user_balance
from keyboards.inline.main_keyboard import accept_order, cancel, admin_keyboard
from utils.db_api.user_controller import get_user_id, update_user_balance_set

from loader import dp


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@dp.callback_query_handler(text_contains='balance', state='*')
async def update_balance(call: CallbackQuery, state: FSMContext):
    await Balance.amount.set()
    await call.message.edit_text('Введите сумму для пополнения:')
    await call.message.edit_reply_markup()


@dp.message_handler(lambda message: isfloat(message.text), state=Balance.amount)
async def get_float_true(message: Message, state: FSMContext):
    await Balance.next()
    await state.update_data(amount=float(message.text))
    await message.answer('Введите id_telegram:')


@dp.message_handler(lambda message: not isfloat(message.text), state=Balance.amount)
async def get_float_false(message: Message, state: FSMContext):
    await message.answer('Неправильно указана сумма пополнения, попробуй еще раз!')


@dp.message_handler(lambda message: message.text.isdigit(), state=Balance.telegram_id)
async def get_float_true(message: Message, state: FSMContext):
    await Balance.next()
    telegram_id = int(message.text)
    await state.update_data(user_id=telegram_id)
    user = await get_user_id(telegram_id)
    if user:
        balance_data = await state.get_data()
        form_message = update_user_balance(balance_data)
        await message.answer(form_message, reply_markup=await accept_order())
    elif user is None:
        await message.answer('Пользователь не найден!', reply_markup=await cancel())


@dp.message_handler(lambda message: not message.text.isdigit(), state=Balance.telegram_id)
async def get_float_false(message: Message, state: FSMContext):
    await message.answer('Неправильно указан id_telegram, попробуй еще раз!')


@dp.callback_query_handler(text_contains='OK', state='*')
async def accept_update(call: CallbackQuery, state: FSMContext):
    balance_data = await state.get_data()
    await state.finish()
    user = await get_user_id(balance_data['user_id'])
    balance = balance_data['amount'] + user.balance
    await update_user_balance_set(balance_data['user_id'], balance)
    await call.message.edit_text('Главное меню:')
    await call.message.edit_reply_markup(reply_markup=await admin_keyboard())
    await call.message.answer('Баланс пользователя обновлен!')