import handlers
from misc import *

async def main() -> None:
    

    print("starting the bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e: 
        print(f'Bot stopped with reason: {e}!')