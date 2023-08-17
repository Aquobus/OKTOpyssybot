from OKTOpyssybot import *

load_dotenv(find_dotenv())

#@dp.message()
#async def default(message: Message) -> None:
    #await message.answer('Выбрано неверное действие')

#@dp.message()
#async def do(message: Message, answer_before: str, answer_after: str, func) -> None:

@dp.message(Command(commands='start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.full_name}</b>! Я - бот, составляющий расписания для нашей группы! Для корректной работы системы и во избежания недопониманий предлагаю выбрать тебе, с кем бы ты хотел быть в паре на дежурстве.")

async def main() -> None:
    print("starting the bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e: 
        print(f'Bot stopped with reason: {e}!')