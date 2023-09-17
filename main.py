from handlers import start, help, echo, chat_id, info, gpt
from callbacks import info_callback, test_callback_factory
from middlewares.notclassmate import NotClassmateMessageMiddleware
from misc import os, asyncio, types, CallbackQuery, Router, F, logger, dp, bot

async def main() -> any:
    command_router = Router()
    callbacks_router = Router()
    other_router = Router()

    command_router.include_routers(
        start.router,
        help.router,
        chat_id.router,
        info.router,
        gpt.router
    )
    callbacks_router.include_routers(
        info_callback.router,
        test_callback_factory.router
    )
    other_router.include_routers(
        echo.router
    )

    dp.include_routers(
        command_router,
        callbacks_router,
        other_router,
    )
    
    command_router.message.middleware(NotClassmateMessageMiddleware())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, kwargs=logger.info('Bot started successfully'))
    except Exception as e:
        logger.error('Something went wrong: ', e)
        raise e('Exception initialised').with_traceback()

if __name__ == "__main__":
    run = asyncio.run(
        main(),
        debug=False
    )
    logger.info('Bot stopped with SIGINT signal\n') 