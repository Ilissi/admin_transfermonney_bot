from aiogram import executor

import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import dp, bot
import functools


async def on_startup(dispatcher, url):
    await bot.delete_webhook()
    await bot.set_webhook(url)
    webhook = await bot.get_webhook_info()
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_webhook(dp, webhook_path='/user_bot/', on_startup=functools.partial(on_startup, url='https://transfermoneybot.ru/user_bot/'), host='127.0.0.1', port=8080)
