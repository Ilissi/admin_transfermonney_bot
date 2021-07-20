from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_keyboard():
    admin = InlineKeyboardMarkup(row_width=3)
    admin.add(InlineKeyboardButton('Статистика', callback_data='stat'))
    admin.add(InlineKeyboardButton('Поиск', callback_data='search'))
    admin.add(InlineKeyboardButton('Пополнение баланса', callback_data='balance'))
    admin.add(InlineKeyboardButton('Рассылка пользователям', callback_data='sender'))
    return admin


async def diapason_statistic():
    diapason = InlineKeyboardMarkup(row_width=3)
    diapason.row(InlineKeyboardButton('День', callback_data='day'), InlineKeyboardButton('Неделя', callback_data='week'))
    diapason.row(InlineKeyboardButton('Месяц', callback_data='Месяц'), InlineKeyboardButton('За все время', callback_data='all_time'))
    diapason.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return diapason


async def search_menu():
    search = InlineKeyboardMarkup(row_width=3)
    search.add(InlineKeyboardButton('Тикер', callback_data='ticker'))
    search.add(InlineKeyboardButton('Пользователь', callback_data='user'))
    search.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return search


async def cancel():
    cancel_button = InlineKeyboardMarkup()
    cancel_button.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return cancel_button


async def accept_order():
    accept_keyboard = InlineKeyboardMarkup()
    accept_keyboard.row(InlineKeyboardButton('OK', callback_data='OK'),
                        InlineKeyboardButton('ОТМЕНА', callback_data='cancel'))
    return accept_keyboard
