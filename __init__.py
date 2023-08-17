import os
import asyncio
import pandas as pd
from dotenv import *
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from commands.help import COMMANDS_DATA as HELP_DATA