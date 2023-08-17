from misc import Command, bot, dp, Message

COMMANDS_DATA = {
    '/start': 'Начало работы с ботом',
    '/help': 'Помощь по командам'
}

@dp.message(Command(commands='help'))
async def commands(message: Message) -> None:
    for command, description in COMMANDS_DATA.items():
        await bot.send_message(message.from_user.id, f'{command}, {description}')