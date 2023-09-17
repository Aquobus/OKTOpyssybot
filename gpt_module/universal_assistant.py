import asyncio

from misc import logger
from characterai import PyAsyncCAI
from typing import Any

char = 'YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8'
client = PyAsyncCAI("14e8586bb83c7c0b64c77ffe72de54b0f75c0388")
chat = None
tgt = None
participants = None

class Character():
    def __init__(self):
        self.char         = 'YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8',
        self.client       = PyAsyncCAI("14e8586bb83c7c0b64c77ffe72de54b0f75c0388")
        self.chat         = Any | str
        self.tgt          = Any | str
        self.participants = Any | str

    async def init(self, headless: bool = True):
        await self.client.start(headless=headless)
        
        self.chat = await self.client.chat.get_chat(char)
        self.participants = self.chat['participants']

        if not self.participants[0]['is_human']:
            self.tgt = self.participants[0]['user']['username']
        else:
            self.tgt = self.participants[1]['user']['username']

        return self
    
    async def send(self, send_message: str = "") -> list:
        message = send_message
        data    = await self.client.chat.send_message(
            self.chat['external_id'],
            self.tgt,
            message
        )

        name  = data['src_char']['participant']['name']
        text  = data['replies'][0]['text']
        list_ = [name, text, True]

        return list_
    
    async def print_chat(self):
        print(self.chat)
        print(self.chat['external_id'])

async def start():
    character = Character()
    await character.init()

    logger.info('Chatbot initialised')

    return character