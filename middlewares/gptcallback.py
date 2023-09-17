import os
from misc import logger, random, CallbackQuery, ParseMode
from dotenv import load_dotenv, find_dotenv
from functions.OktyBotMain import is_in_group
from typing import Callable, Dict, Any, Awaitable, Union
from aiogram import BaseMiddleware

class GptCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]) -> Any:
        
        return await handler(event, data)

