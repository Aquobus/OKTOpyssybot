import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from aiogram import Router
from . import whatisithmmmm as whaat
from aiogram.types import Message
from aiogram.filters import Command
from functions.OktyBotMain import id_to_name

router = Router()

@router.message()
async def echo(message: Message) -> None:
    if '!' in str(message.text):
        return True
    if len(str(message.text)) < 3:
        await message.answer(message.text)
        return True
    if str(message.text).lower() in list(whaat.HM.keys()):
        await message.answer(whaat.HM[str(message.text).lower()])
        return True
    for i in list(whaat.HM.keys()):
        if str(message.text).lower() in i or i in str(message.text).lower():
            await message.answer(whaat.HM[i])
            return True
    await message.answer(message.text)

    return None
    
    