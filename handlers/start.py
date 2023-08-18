import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pandas as pd
from main import bot
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from functions.OktyBotMain import id_to_name
from middlewares.notclassmate import NotClassmateCallbackMiddleware

router = Router()

@router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    name = id_to_name(str(message.from_user.id))
    await message.answer(f"Привет, <b>{name}</b>! Я - бот, составляющий расписания для нашей группы! Для корректной работы системы и во избежания недопониманий предлагаю выбрать тебе, с кем бы ты хотел быть в паре на дежурстве.")