from __init__ import *
import discord_commands

if __name__ == '__main__':
    discord_commands.run(config.get('DiscordSection','token'))