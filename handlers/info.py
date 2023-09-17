from misc import os, Command, Message, Router, load_dotenv, find_dotenv
from aiogram.enums.parse_mode import ParseMode

load_dotenv(find_dotenv())

TEXT = os.environ.get('INFO_TEXT')
router = Router()

@router.message(Command('info'))
async def info(message: Message) -> None:
    await message.answer(TEXT, parse_mode=ParseMode.HTML)