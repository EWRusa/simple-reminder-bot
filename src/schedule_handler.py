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

#scheduled reminder
async def add_single_reminder(reminder_time, event, context, target):
    scheduler.add_job(
        send_reminder,
        'date',
        next_run_time=time_converter(reminder_time),
        args=[event, context, target],
        id = id_creator(event, target)
    )

#cronjob reminder
async def add_cron_reminder(minute, hour, day, month, day_of_week, event, context, target):
    scheduler.add_job(
        send_reminder,
        'cron',
        minute = minute,
        hour = hour,
        day = day,
        month = month,
        day_of_week = day_of_week,
        args=[event, context, target],
        id = id_creator(event, target)
    )

#helpers
def id_creator(event, target):
    event_id = str.replace(event,' ', '_')
    return f'{event_id}_{target}'

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