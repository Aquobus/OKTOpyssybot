from misc import Command, bot, Message
from aiogram import Router

COMMANDS_DATA = {
    '/start': 'Начало работы с ботом',
    '/help': 'Помощь по командам'
}

router = Router()

@router.message(Command(commands='id'))
async def return_id(message: Message) -> int:
    await message.answer(f'ID чата: {message.chat.id}')