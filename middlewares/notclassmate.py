import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions.OktyBotMain import add_to_blacklist, is_in_group
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update

class NotClassmateMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]) -> Any:
        if is_in_group(userid=event.from_user.id):
            return await handler(event, data)
            print('Пользователь есть в базе данных!')
        
        await event.answer(
            "Пользователь не найден в базе!",
            show_alert=True
        )
        return

class NotClassmateCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        if is_in_group(userid=0):
            return await handler(event, data)
            await event.answer('Пользователь есть в базе данных!')
        
        await event.answer(
            "Пользователь не найдет в базе данных!",
            show_alert=True
        )
        return