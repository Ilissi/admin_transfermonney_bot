from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URL


db = Gino()

async def create_db():
    await db.set_bind(POSTGRES_URL)
    db.gino: GinoSchemaVisitor
