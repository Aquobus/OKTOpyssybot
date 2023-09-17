from misc import Router, Command, Message, F, bot, asyncio
from aiogram.enums import ChatAction
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from gpt_module import universal_assistant as assist

from typing import Any

router = Router()
class OrderToSendingRequest(StatesGroup):
    prepare_to_send_request = State()
    sending_request = State()

@router.message(Command('gpt'))
async def gpt(message: Message, state: FSMContext) -> None:
    kb = [
        [
            KeyboardButton(text='Написать боту'),
            KeyboardButton(text='Выйти из режима GPT')
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Напишите сообщение чатботу"
    )
    data = await state.get_data()
    if data == {}:
        character = await assist.start()
        await state.update_data(character_obj=character)
    else:
        pass

    await state.set_state(OrderToSendingRequest.prepare_to_send_request) # Ставим первое состояние на входную команду, чтобы навесить его на первый хендлер клавиатуры и в будущем вернуться к этому хендлеру
    
    await message.answer(
        f"Вы вошли в режим общения с чатботом!",
        reply_markup=keyboard
    )

@router.message(OrderToSendingRequest.prepare_to_send_request, F.text.lower() == "написать боту") # Мы навесили условие для сообщения - состояние prepare_to_send_request, чтобы вернуться к этому состоянию в будущем
async def prepare_send_request(message: Message, state: FSMContext) -> None:
    await message.answer('Введи сообщение, которое хочешь отправить')
    await state.set_state(OrderToSendingRequest.sending_request) # Состояние отправки запроса

@router.message(OrderToSendingRequest.sending_request)
async def send_request(message: Message, state: FSMContext) -> None:
    character_objects = await state.get_data()
    character = character_objects['character_obj']
    if character == Any:
        await message.answer('character is empty')
    else:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        result = await character.send(send_message=str(message.text))
        await bot.send_message(message.chat.id, f"{result[1]}")
    await state.set_state(OrderToSendingRequest.sending_request)

@router.message(F.text.lower() == "выйти из режима gpt" or OrderToSendingRequest.sending_request or OrderToSendingRequest.prepare_to_send_request or Command('/exit'))
async def exit_gpt(message: Message, state: FSMContext) -> None:
    await message.answer('Успех!', reply_markup=ReplyKeyboardRemove())
    await state.clear() # Очистка всех состояний и удаление клавиатуры
