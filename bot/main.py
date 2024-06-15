import logging
import os
import asyncio
import sys
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv('../.env')
TOKEN = os.getenv('BOT_TOKEN')
ADMIN = os.getenv('ADMINS_CHANNEL_ID')

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

API_ENDPOINT = 'http://127.0.0.1:8000/api/'
already_orders = set()


# Define message handlers
@router.message(CommandStart())
async def send_hello(message: Message):
    await message.answer("Hello! I am Mahorat.uz personal assistant.")


@router.message(Command(commands=['employee']))
async def send_employee(message: Message):
    await message.answer("employee command")


@router.message(Command(commands=['message']))
async def send_message_command(message: Message):
    await message.answer('message command')


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


# Entry point of the script
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
