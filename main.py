from handlers import start, help
from middlewares.notclassmate import NotClassmateCallbackMiddleware, NotClassmateMessageMiddleware
from misc import *

async def main() -> None:
    print("starting the bot...")
    dp.include_routers(start.router, help.router)
    dp.message.middleware(NotClassmateMessageMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e: 
        print(f'Bot stopped with reason: {e}!')