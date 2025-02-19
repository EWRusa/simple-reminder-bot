from __init__ import *
import bot_handler
import schedule_handler
import asyncio

async def routine_starter():
    await schedule_handler.start()
    await bot_handler.start(config.get('DiscordSection', 'token'))

if __name__ == '__main__':
    asyncio.run(routine_starter())