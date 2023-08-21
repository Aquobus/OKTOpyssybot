from misc import Command, Message
from aiogram import Router

COMMANDS_DATA = {
    '/start': 'Начало работы с ботом',
    '/help': 'Помощь по командам'
}

router = Router()

@router.message(Command('help'))
async def help(message: Message) -> None:
    for command, description in COMMANDS_DATA.items():
        await message.answer(message.from_user.id, f'{command}, {description}')