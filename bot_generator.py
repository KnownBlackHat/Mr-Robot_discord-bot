
# Argument Format: python bot_generator.py <token var name> <status no.> <name> <bot=True|False>

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
    return client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=sys.argv[3]))

  elif sys.argv[2] == '2':
    # Setting `Streaming ` status
    return client.change_presence(activity=discord.Streaming(name=sys.argv[3], url="https://discord.gg/yuwTXBadzK"))

  elif sys.argv[2] == '3':
    # Setting `Listening ` status
    return client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=sys.argv[3]))

  elif sys.argv[2] == '4':
    # Setting `Watching ` status
    return client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=sys.argv[3]))

    
@client.event
async def on_ready():
    print(f'\n [!] Logged in as {client.user}')
    await get_cmd()
#     await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='OUR WORLD GETTING HACKED'))
if sys.argv[4].lower() == 'true':
  is_bot = True
else:
  is_bot = False
client.run(os.getenv(f"{sys.argv[1]}"), bot=is_bot)
