from OKTOpyssybot import Command, Message, dp, bot

@dp.message(Command(commands='start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Я - бот, составляющий расписания для нашей группы! Для корректной работы системы и во избежания недопониманий предлагаю выбрать тебе, с кем бы ты хотел быть в паре на дежурстве.")