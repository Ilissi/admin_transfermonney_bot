from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import CallbackQuery

from keyboards.inline.main_keyboard import admin_keyboard
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(text=f'Привет, {message.from_user.full_name}!', reply_markup=await admin_keyboard())


@dp.callback_query_handler(text_contains='cancel', state='*')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def back_main_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(f'Привет, {call.from_user.full_name}!')
    await call.message.edit_reply_markup(reply_markup=await admin_keyboard())
