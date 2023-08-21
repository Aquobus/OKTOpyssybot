from handlers import start, help, echo, chat_id
from middlewares.notclassmate import NotClassmateMessageMiddleware
from misc import os, asyncio, Router, logger, dp, bot

async def main() -> any:
    command_router = Router()
    command_router.include_routers(
        start.router,
        help.router,
        chat_id.router
    )

    command_router.message.middleware(NotClassmateMessageMiddleware())

    dp.include_routers(
        command_router,
        echo.router
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, kwargs=logger.info('Bot started successfully'))
    except Exception as e:
        logger.error('Something went wrong: ', e)
        raise e('Exception initialised').with_traceback()

if __name__ == "__main__":
    try:
        run = asyncio.run(main(), debug=True)
        logger.info('Bot stopped with SIGINT signal')
    except (KeyboardInterrupt, SystemExit, Exception) as e: 
        logger.error('Bot stopped with reason', exc_info=True)