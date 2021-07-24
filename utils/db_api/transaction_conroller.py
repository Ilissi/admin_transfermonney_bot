from utils.db_api.models import Transactions


async def get_transaction(transaction_id):
    transaction = await Transactions.query.where(Transactions.id == transaction_id).gino.first()
    return transaction


async def update_transaction(transaction_id, status_value):
    transaction = await Transactions.update.values(status=status_value).where(Transactions.id == transaction_id).gino.status()
    return transaction

