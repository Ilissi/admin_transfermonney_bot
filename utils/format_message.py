async def format_counter_message(title, values_dict):
    message_format = '<b>{title}</b>\n<b>Количество сделок:</b> {count}\n<b>Сумма сделок:</b> {amount}'.format(
        title=title, count=values_dict['count'], amount=values_dict['amount'])
    return message_format


def show_message(data_dict):
    str_data = '<b>ID заказа:</b> {id}\n<b>Валюта перевода:</b> {get_currency}\n<b>Страна перевода:</b> {get_country}\n<b>Сумма перевода:</b> {amount_get}\n<b>Номер карты получателя:</b> {card_number}\n<b>ФИО получателя:</b> {FIO}\n<b>Сумма списания со счета:</b> {summary}$ \n<b>Статус:</b> {status}'.format(
        id=data_dict.id, get_currency=data_dict.currency_get, get_country=data_dict.country_get, amount_get=data_dict.amount_get,
        card_number=data_dict.card_number, FIO=data_dict.FIO, summary=data_dict.amount_spend, status=data_dict.status)
    return str_data


def user_message(data_dict):
    str_data = '<b>id_telegram: </b>{id_telegram}\n<b>username: </b>{username}\n<b>Баланс: </b>{balance}\n<b>Зарегистрирован: </b>{time_registered}'.format(
        id_telegram=data_dict.id_telegram, username=data_dict.username, balance=data_dict.balance, time_registered=str(data_dict.time_registered).split('.')[0]
    )
    return str_data


def update_user_balance(data_dict):
    str_data = '<b>id_telegram: </b>{id_telegram}\n<b>Сумма пополнения: </b>{balance}'.format(
        id_telegram=data_dict['user_id'], balance=data_dict['amount']
    )
    return str_data