import os, sys, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from misc import logger, random
from dotenv import load_dotenv, find_dotenv
from functions.OktyBotMain import is_in_group
from typing import Callable, Dict, Any, Awaitable

load_dotenv(find_dotenv())

from aiogram import BaseMiddleware
from aiogram.types import Message

phrases = os.environ.get('PHRASES').split(';')

class NotClassmateMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]) -> Any:
        if is_in_group(userid=event.from_user.id):
            logger.info(f'Interacts with a user who has in database.\nUSER ID: {data["event_from_user"].id}\nUSERNAME: {data["event_from_user"].username}\nFROM CHAT: {data["event_chat"].title or data["event_chat"].username}\nMESSAGE: {event.text}\n')

            await data["bot"].send_message(
                chat_id=-849888674,
                text=f'Interacts with a user who has in database.\nUSER ID: {data["event_from_user"].id}\nUSERNAME: {data["event_from_user"].username}\nFROM CHAT: {data["event_chat"].title or data["event_chat"].username}\nMESSAGE: {event.text}\n'
            )

            return await handler(event, data)
        
        await event.answer(
            phrases[random.randint(0, len(phrases)-1)],
            show_alert=True
        )
        logger.warning(f'Achtung! Alarm! An unknown user is trying to interact with the bot!\nUser ID: {data["event_from_user"].id}\nUSERNAME: {data["event_from_user"].username}\nFROM CHAT: {data["event_chat"].title or data["event_chat"].username}\nMESSAGE: {event.text}\n')
        return