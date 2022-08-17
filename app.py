from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands

if __name__ == '__main__':
    executor.start_webhook(dp)
