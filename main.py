from OKTOpyssybot import *

load_dotenv(find_dotenv())

#@dp.message()
#async def default(message: Message) -> None:
    #await message.answer('Выбрано неверное действие')

#@dp.message()
#async def do(message: Message, answer_before: str, answer_after: str, func) -> None:

async def main() -> None:
    print("starting the bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e: 
        print(f'Bot stopped with reason: {e}!')