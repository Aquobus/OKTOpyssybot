# Судя по тому, что мне написал Dany2k, для этой задачи мы должны использовать:
# Фабрику колбэков
# FSM

CALLBACK_DATA = {
    'days': ('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ'),
    'pupil': ('Ротарь', 'Лопатюк'),
    'reason': ('Съебался', 'По причине', 'Отсутствовал', 'Заболел'),
    'replace_method': ('Вручную', 'Авто')
}

from misc import Router, Command, Message, Bot, F
from . import callback_fab as fab
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

router = Router()
day_keyboard = InlineKeyboardBuilder()

class CallbackDataCollector():
    def __init__(self):
        self.day: str = "",
        self.pupil: str = "",
        self.reason: str = "",
        self.replace_method: str = ""

collector = CallbackDataCollector()

day_keyboard.button(
    text=CALLBACK_DATA['days'][0], callback_data=CALLBACK_DATA['days'][0]
)
day_keyboard.button(
    text=CALLBACK_DATA['days'][1], callback_data=CALLBACK_DATA['days'][1]
)
day_keyboard.button(
    text=CALLBACK_DATA['days'][2], callback_data=CALLBACK_DATA['days'][2]
)
day_keyboard.button(
    text=CALLBACK_DATA['days'][3], callback_data=CALLBACK_DATA['days'][3]
)
day_keyboard.button(
    text=CALLBACK_DATA['days'][4], callback_data=CALLBACK_DATA['days'][4]
)
day_keyboard.adjust(2)

pupil_keyboard = InlineKeyboardBuilder()
pupil_keyboard.button(
    text=CALLBACK_DATA['pupil'][0], callback_data=CALLBACK_DATA['pupil'][0]
)
pupil_keyboard.button(
    text=CALLBACK_DATA['pupil'][1], callback_data=CALLBACK_DATA['pupil'][1]
)
pupil_keyboard.adjust(1)

reason_keyboard = InlineKeyboardBuilder()
reason_keyboard.button(
    text=CALLBACK_DATA['reason'][0], callback_data=CALLBACK_DATA['reason'][0]
)
reason_keyboard.button(
    text=CALLBACK_DATA['reason'][1], callback_data=CALLBACK_DATA['reason'][1]
)
reason_keyboard.button(
    text=CALLBACK_DATA['reason'][2], callback_data=CALLBACK_DATA['reason'][2]
)
reason_keyboard.button(
    text=CALLBACK_DATA['reason'][3], callback_data=CALLBACK_DATA['reason'][3]
)
reason_keyboard.adjust(2)

replace_method_keyboard = InlineKeyboardBuilder()
replace_method_keyboard.button(
    text=CALLBACK_DATA['replace_method'][0], callback_data=CALLBACK_DATA['replace_method'][0]
)
replace_method_keyboard.button(
    text=CALLBACK_DATA['replace_method'][1], callback_data=CALLBACK_DATA['replace_method'][1]
)
replace_method_keyboard.adjust(1)

confirm_keyboard = InlineKeyboardBuilder()
confirm_keyboard.button(
    text='Подтвердить', callback_data="finish"
)

@router.callback_query(F.data == 'change_user_start')
async def start_change(callback: CallbackQuery) -> str:
    await callback.message.answer('Выбери день', reply_markup=day_keyboard.as_markup(resize_keyboard=True))

@router.callback_query(F.data.in_(CALLBACK_DATA['days']))
async def choose_pupil(callback: CallbackQuery) -> str:
    await callback.message.answer('Теперь ебани челика', reply_markup=pupil_keyboard.as_markup(resize_keyboard=True))
    collector.day = callback.data

@router.callback_query(F.data.in_(CALLBACK_DATA['pupil']))
async def choose_reason(callback: CallbackQuery) -> str:
    await callback.message.answer('Выбери причину', reply_markup=reason_keyboard.as_markup(resize_keyboard=True))
    collector.pupil = callback.data

@router.callback_query(F.data.in_(CALLBACK_DATA['reason']))
async def choose_replace_method(callback: CallbackQuery) -> str:
    await callback.message.answer('Выбери способ замены', reply_markup=replace_method_keyboard.as_markup(resize_keyboard=True))
    collector.reason = callback.data

@router.callback_query(F.data.in_(CALLBACK_DATA['replace_method']))
async def confirm_and_finish(callback: CallbackQuery) -> str:
    await callback.message.answer('Подтвердить?', reply_markup=confirm_keyboard.as_markup(resize_keyboard=True))
    collector.replace_method = callback.data

@router.callback_query(F.data == "finish")
async def return_result(callback: CallbackQuery) -> str:
    await callback.message.answer(f'Результат: {collector.day} {collector.pupil} {collector.reason} {collector.replace_method}')