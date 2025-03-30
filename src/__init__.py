import configparser
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler

my_intents = discord.Intents.default()
my_intents.message_content = True
bot_version = '0.2'
config = configparser.ConfigParser()
config.read('../resources/application.properties')
scheduler = AsyncIOScheduler()