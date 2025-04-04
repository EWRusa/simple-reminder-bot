import asyncio
import logging
import schedule_handler

from __init__ import *
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=my_intents, allowed_mentions= discord.AllowedMentions(everyone=True))
#logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

@bot.command(name='version', help='Returns app version.')
async def version(context):
    async with context.typing():
        log_event(context)
        await asyncio.sleep(1)
    await context.send(f'`SimpleReminderBot Version: {bot_version}`')

@bot.command(name='remindme', help='Sets a reminder for yourself, usage is as follows \"!remindme <event> HH:MM MM/DD/YYYY\".')
async def remind_me(context, event, time, date):
    async with context.typing():
        log_event(context)
        await add_reminder(time, date, event, context, context.author.mention)

@bot.command(name='remindall', help='Sets a reminder for everyone, usage is as follows \"!remindme <event> HH:MM MM/DD/YYYY\".')
async def remind_all(context, event, time, date):
    async with context.typing():
        log_event(context)
        await add_reminder(time, date, event, context, context.message.guild.default_role)

# Events
@bot.event
async def on_connect():
    logger.info(f'Connected discord bot.')

@bot.event
async def on_ready():
    logger.info(f'Started discord bot successfully. Discord bot ready.')

# Exception Handling
@bot.event
async def on_command_error(context, error):
    await context.send(f'An error occurred while attempting to execute this command, please refer to the help for this command by using `!help <command_name>` or `!help` for all commands.\n{error}')

#helpers
async def add_reminder(time, date, event, context, target):
    await schedule_handler.add_reminder(date_time_combiner(time, date), event, context, target)
    await context.send(f'Set a reminder for \"{event}\" at {time} on {date}!')

def log_event(context):
    logger.info(f'Received {context.command} request from \"{context.guild.name}\" sent by \"{context.author.name}\"')

def date_time_combiner(time, date):
    return f'{date} {time}'

# starters
async def start(token):
    logger.info(f'Starting discord bot.')
    try:
        await bot.start(token)
    except:
        logger.error(f'Discord bot failed to start.')