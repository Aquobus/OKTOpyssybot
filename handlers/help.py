from misc import Command, bot, Message
from aiogram import Router

COMMANDS_DATA = {
    '/start': 'Начало работы с ботом',
    '/help': 'Помощь по командам'
}

router = Router()

@router.message(Command(commands='help'))
async def commands(message: Message) -> None:
    for command, description in COMMANDS_DATA.items():
        await bot.send_message(message.from_user.id, f'{command}, {description}')