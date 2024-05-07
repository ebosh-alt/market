from aiogram import Dispatcher, Bot
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InputFile, FSInputFile
from environs import Env


env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')
dp = Dispatcher()
bot = Bot(bot_token)
PAYMENTS_PROVIDER_TOKEN = '390540012:LIVE:45899'
DATABASE_URL = f'sqlite+aiosqlite:///data/database.db'
OFFER = FSInputFile("data/Оферта.docx")

# callback_yes = CallbackData('yes', 'user_id', 'time', 'day', 'month', 'year', 'new_id')
# callback_no = CallbackData('no', 'user_id', 'time', 'day', 'month', 'year', 'new_id')
# callback_yes_sam = CallbackData('yes_sam', 'user_id', 'time', 'day', 'month', 'year', 'new_id')
# callback_moder = CallbackData('moder', 'user_id', 'time', 'day', 'month', 'year', 'new_id')
# callback_no_sam = CallbackData('no_sam', 'user_id', 'time', 'day', 'month', 'year', 'new_id')
# callback_check = CallbackData('check', 'num')