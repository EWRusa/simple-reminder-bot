from __init__ import *
import asyncio
import datetime
import logging

#logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

async def send_reminder(event, context, target):
    await context.send(f'{target} this is your reminder for {event}.')

async def add_reminder(reminder_time, event, context, target):
    scheduler.add_job(send_reminder, 'date', next_run_time=time_converter(reminder_time), args=[event, context, target])

#helpers
def time_converter(reminder_time):
    reminder_time_obj = datetime.datetime.strptime(reminder_time, '%m/%d/%Y %H:%M')
    return reminder_time_obj

#starters
async def start():
    logger.info(f'Starting scheduler process.')
    try:
        scheduler.start()
        logger.info(f'Started scheduler process successfully. Scheduler ready.')
    except:
        logger.error(f'Scheduler failed to start.')
        exit(1)