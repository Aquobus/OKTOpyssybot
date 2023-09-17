from misc import os, logger, Command, Router, F, CallbackQuery, Bot, ParseMode, load_dotenv, find_dotenv
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

load_dotenv(find_dotenv())

TEXT = os.environ.get('INFO_TEXT')
router = Router()

@router.callback_query(F.data == 'info_command')
async def info_command_callback(callback: CallbackQuery, bot: Bot):
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text='change couple'),
        KeyboardButton(text='me'),
        KeyboardButton(text='week'),
        KeyboardButton(text='history'),
        KeyboardButton(text='test')
    )
    builder.adjust(2)

    await callback.message.answer(
        TEXT,
        reply_markup=builder.as_markup(resize_keyboard=True),
        parse_mode=ParseMode.HTML
    )
    logger.info(f'Callback catched.\n\
CALLBACK ID: {callback.id}\n\
FROM CHAT: {callback.message.chat.title}\n\
CALLBACK DATA: {callback.data}\n\
USER TRIGGERED: @{callback.from_user.username}')
    await bot.send_message(
        chat_id=-849888674,
        text=f'Callback catched.\n\
CALLBACK ID: {callback.id}\n\
FROM CHAT: {callback.message.chat.title}\n\
CALLBACK DATA: {callback.data}\n\
USER TRIGGERED: @{callback.from_user.username}',
        parse_mode=ParseMode.HTML
    )