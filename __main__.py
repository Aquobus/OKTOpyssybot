import os
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message
from command import COMMANDS_DATA
from . import botsTokens as tokens

TOKEN      = tokens.USER_TOKEN
dp         = Dispatcher()
bot        = Bot(TOKEN, parse_mode="HTML")

#@dp.message()
#async def default(message: Message) -> None:
    #await message.answer('Выбрано неверное действие')

#@dp.message()
#async def do(message: Message, answer_before: str, answer_after: str, func) -> None:


@dp.message(Command(commands='help'))
async def commands(message: Message) -> None:
    for command, description in COMMANDS_DATA.items():
        await bot.send_message(message.from_user.id, f'{command}, {description}')

@dp.message(Command(commands='start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Я - бот, составляющий расписания для нашей группы! Для корректной работы системы и во избежания недопониманий предлагаю выбрать тебе, с кем бы ты хотел быть в паре на дежурстве.")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e: 
        print(f'Bot stopped with reason: {e}!')