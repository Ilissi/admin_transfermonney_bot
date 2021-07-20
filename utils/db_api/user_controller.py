from utils.db_api.models import Users
from typing import List


async def get_all_users() -> List[Users]:
    orders = await Users.query.gino.all()
    return orders


async def get_user(username) -> Users:
    users = await Users.query.where(Users.username == username).gino.first()
    return users


async def get_user_id(telegram_id) -> Users:
    users = await Users.query.where(Users.id_telegram == telegram_id).gino.first()
    return users


async def update_user_balance_set(telegram_id, balance):
    transaction = await Users.update.values(balance=balance).where(Users.id_telegram == telegram_id).gino.status()
    return transaction

