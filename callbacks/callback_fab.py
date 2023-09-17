from typing import Optional
from aiogram.filters.callback_data import CallbackData

class ToChangeCallbackFactory(CallbackData, prefix="change"):
    action: str
    value: Optional[str] = None