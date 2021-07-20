from typing import List
from sqlalchemy import and_

from utils.db_api.models import Orders


async def get_orders(ticker_id) -> List[Orders]:
    orders = await Orders.query.where(Orders.id == ticker_id).gino.all()
    return orders


async def get_orders_by_date(get_day):
    orders = await Orders.query.where(Orders.time_ordered >= get_day.date()).gino.all()
    return orders


async def get_order_by_diapason(from_date, to_date):
    orders = await Orders.query.where(and_(Orders.time_ordered >= from_date, Orders.time_ordered <= to_date)).gino.all()
    return orders


async def get_all_orders():
    orders = await Orders.query.gino.all()
    return orders

