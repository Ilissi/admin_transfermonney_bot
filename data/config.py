from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
BOT_TOKEN = '1922146668:AAHME-AxbZInHNtDcKjYYVO1PvvFoR8OweI'
ADMIN_BOT = '1849927581:AAE31wEKYZ-3bbsFWjzC35nAIMW-gDZnayI'
ADMINS = [474053240]
IP = 'localhost'
PG_USER = 'postgres'
PG_PASSWORD = 'vick1715'
DATABASE = 'botapp'
MERCHANT_ID = 'e9d0f828c9b8b52f00631e4b6789b0fb'
SECRET = 'a4533e9799acd0e92a9800c20a10d556'
QIWI_API_KEY = '4388de24c629234586e618ee92370796'
QIWI_NUMBER = '+7 999 925‑62‑05'
ITEM_NAME = 'MoneyTransfer'

POSTGRES_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{IP}/{DATABASE}"
