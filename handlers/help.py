from misc import Command, Message
from aiogram import Router
from aiogram.enums.parse_mode import ParseMode

COMMANDS_DATA = {
    '/start': 'Начало работы с ботом',
    '/help': 'Помощь по командам',
    '/info': 'Вывести полную информацию о боте',
    '/gpt': 'Перейти в режим общения с чатботом ()',
    '/exit': 'Выйти из режима общения с чатботом (если кнопка не работает)',
    '/id': 'Узнать ID текущего чата',
    '/me': 'Вывести статистику о себе',
    '/change_couple': 'Команда для изменения напарника по дежурству',
    '/history': 'Полная история дежурств в формате .xlsx',
    '/week': 'Список дежурных на этой неделе'
}

router = Router()

@router.message(Command('help'))
async def help(message: Message) -> None:
    for command, description in COMMANDS_DATA.items():
        await message.answer(f'{command}, {description}', parse_mode=ParseMode.HTML)