from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext

from states.send_message import Message
from utils.db_api.user_controller import get_all_users
from loader import dp, bot_admin


@dp.callback_query_handler(text_contains='sender', state='*')
async def stat_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await Message.message.set()
    await call.message.edit_text('Введите сообщения для рассылки:')
    await call.message.edit_reply_markup()


@dp.message_handler(state=Message.message)
async def send_message(message: Message, state: FSMContext):
    await state.finish()
    message_send = message.text
    users = await get_all_users()
    try:
        for user in users:
            await bot_admin.send_message(user.id_telegram, message_send)
    except:
        pass
    await message.answer('Рассылка успешна!')