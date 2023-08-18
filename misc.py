import os
import random
import asyncio
import openpyxl
import pandas as pd
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv

env   = load_dotenv(find_dotenv())
TOKEN = os.environ.get('ADM_TOKEN')
dp    = Dispatcher()
bot   = Bot(TOKEN, parse_mode="HTML")