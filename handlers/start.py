from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from functions.OktyBotMain import id_to_name, return_pupils

pupils = return_pupils()
router = Router()

@router.message(Command('start'))
async def start(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text='Info', callback_data='info_command'),
        InlineKeyboardButton(text='Тестовая кнопка', callback_data='change_user_start')
    )

    name = id_to_name(str(message.from_user.id))
    await message.answer(
        f"Привет, {name}!\nПосмотри информацию:",
        reply_markup=builder.as_markup()    
    )