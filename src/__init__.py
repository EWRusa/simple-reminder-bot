import configparser
import discord

my_intents = discord.Intents.default()
my_intents.message_content = True
bot_version = '0.1'
config = configparser.ConfigParser()
config.read('../resources/application.properties')