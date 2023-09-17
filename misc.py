import os
import random
import asyncio
import openpyxl
import pandas as pd
from loguru import logger
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv, find_dotenv

env   = load_dotenv(find_dotenv())
TOKEN = os.environ.get('ADM_TOKEN')
dp    = Dispatcher()
bot   = Bot(TOKEN, parse_mode="HTML")

logger.add(
    os.environ.get('LOGGING_PATH'),
    level='INFO',
    enqueue=True,
    format='{time: HH:mm:ss} {level} {message}',
    rotation='10 MB',
    encoding='UTF-8')