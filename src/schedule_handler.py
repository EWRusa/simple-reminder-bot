from __init__ import *
import asyncio
import datetime
import logging

#logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

def time_converter(reminder_time):
    print(f'TODO, convert time')
    reminder_time_obj = datetime.datetime.strptime(reminder_time, '%m/%d/%Y %H:%M')
    return reminder_time_obj

async def send_reminder(context, target):
    print(f'reminder notif')
    await context.send(f'{target} this is your sample reminder.')

async def add_reminder(reminder_time, context, target):
    print(f'TODO, make scheduler')
    scheduler.add_job(send_reminder, 'date', next_run_time=time_converter(reminder_time), args=[context, target])

#helper and start

async def start():
    logger.info(f'Starting scheduler process.')
    try:
        scheduler.start()
        logger.info(f'Started scheduler process successfully. Scheduler ready.')
    except:
        logger.error(f'Scheduler failed to start.')
        exit(1)