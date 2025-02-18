from discord import DiscordException

from __init__ import *
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=my_intents)

@bot.command(name='version', help='Returns app version.')
async def version(ctx):
    await ctx.send(f'`SimpleReminderBot Version: {bot_version}`')

@bot.command(name='remindme', help='Sets a reminder for yourself, usage is as follows \"!remindme <event> HH:MM MM/DD/YYYY\".')
async def remind_me(ctx, event, time, date):
    await ctx.send(f'Set a reminder for \"{event}\" at {time} on {date}! (this doesn\'t work yet)')

@bot.command(name='remindall', help='Sets a reminder for everyone, usage is as follows \"!remindme <event> HH:MM MM/DD/YYYY\".')
async def remind_all(ctx, event, time, date):
    await ctx.send(f'Set a reminder for \"{event}\" at {time} on {date}! (this doesn\'t work yet)')

# Exception Handling
@bot.event
async def on_command_error(ctx,error):

    await ctx.send('An error occurred while attempting to execute this command, please refer to the help for this command by using `!help <command_name>` or `!help` for all commands.')

def run(token):
    bot.run(token)