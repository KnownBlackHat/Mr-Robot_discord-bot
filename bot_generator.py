
# Argument Format: python bot_generator.py <token no.> <status no.> <name> 

import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv()
import os
import sys
client = commands.Bot(command_prefix=':',intents = discord.Intents.all(),self_bot=True)
def get_cmd():
  if sys.argv[2] == '1':
    # Setting `Playing` status
    return bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=sys.argv[3]))

  elif sys.argv[2] == '2':
    # Setting `Streaming ` status
    return bot.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=sys.argv[3], url="https://www.twitch.tv/amouranth"))

  elif sys.argv[2] == '3':
    # Setting `Listening ` status
    return bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=sys.argv[3]))

  elif sys.argv[2] == '4':
    # Setting `Watching ` status
    return bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=sys.argv[3]))

    
@client.event
async def on_ready():
    print(f'\n [!] TOKEN{sys.argv[1]} Logged in as {client.user}')
    await get_cmd()
#     await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='OUR WORLD GETTING HACKED'))
client.run(os.getenv(f"TOKEN{sys.argv[1]}"), bot=False)
