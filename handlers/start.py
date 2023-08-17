import pandas as pd
from main import dp, bot
from aiogram.types import Message
from aiogram.filters import Command

dataframe = pd.read_excel('/home/aquobus/dev/OKTOpyssybot/DB/main.xlsx')

@dp.message(Command(commands='start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Я - бот, составляющий расписания для нашей группы! Для корректной работы системы и во избежания недопониманий предлагаю выбрать тебе, с кем бы ты хотел быть в паре на дежурстве.")