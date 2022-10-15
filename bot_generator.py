import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv()
import os
import sys
client = commands.Bot(
  command_prefix=':',intents = discord.Intents.all(),
  self_bot=True
)
@client.event
async def on_ready():
    print(f'\n [!] TOKEN{sys.argv[1]} Logged in as {client.user}')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='OUR WORLD GETTING HACKED'))
client.run(os.getenv(f"TOKEN{sys.argv[1]}"), bot=False)
