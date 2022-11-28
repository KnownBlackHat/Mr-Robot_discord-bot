# import logging

# logger = logging.getLogger('disnake')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

# MODULES IMPORT
import os
from main import proxy_generator as proxy
import datetime
import time
import asyncio
# from webserver import keep_alive
import disnake
from disnake.client import Client
from disnake.ext import tasks, commands
import random
from dotenv import load_dotenv
import json
# VARIABLE INIT
proxy=proxy()
start_time = time.time()
# def get_prefix(client,message):
#     try:
#       with open('greeting_channel.json','r') as file:
#           prefixes=json.load(file)
#       try:
#           prefixes[str(message.guild.id)]["prefix"]
#       except:
#           prefixes[str(message.guild.id)]["prefix"] = "!!"
#           json.dump(prefixes,open('greeting_channel.json','w'),indent=2)
#       return commands.when_mentioned_or(prefixes[str(message.guild.id)]["prefix"])(client,message)
#     except:
#       return commands.when_mentioned_or("!!")(client,message)
      

client = commands.Bot(proxy=proxy, command_prefix=commands.when_mentioned,intents = disnake.Intents.all())
load_dotenv()

# EVENTS


error = ''
unloaded_cog_list=[]
loaded_cog_list= []

class cr:
    red = 0xff0000
    green = 0x00ff00
    blue = 0x0000ff
    black = 0x000000
    orange = 0xffa500
    yellow = 0xffff00
    @staticmethod
    def emb(color=green, name='', value=''):
        Em = disnake.Embed(color=color, title=name, description=value)
        Em.timestamp = datetime.datetime.utcnow()
        Em.set_footer(text="MR ROBOT", icon_url="https://www.logolynx.com/images/logolynx/17/17688231e794e005ef6511061bd9f1c0.jpeg")
        return Em


try:
    for file in os.listdir('Cogs'):
        if file.endswith('.py'):
            try:
                client.load_extension(f'Cogs.{str(file[:-3])}')
                loaded_cog_list.append(file[:-3])
            except Exception as e:
                print(e)
                unloaded_cog_list.append(file[:-3])

except Exception as error:
    with open('Logs/error.log','a') as file:
      file.write(f'\nCogs Error: {error}')
@client.remove_command('help')


# @tasks.loop(hours=1)
# async def bot_alive():
#       os.system("pkill bot_generator.py")
#       os.system('python bot_generator.py Known_Black_Hat 1 "Our World Getting Hacked" false & ')
#       os.system('python bot_generator.py Cyber_Girl 4 "Over This Server" false & ')
#       os.system('python bot_generator.py Desus 2 "@Ping For Help" false & ')
            
            
@commands.is_owner()
@client.slash_command(description="Shows all loaded Cogs",guild_ids=[1003683013625925664])
async def list_functions(ctx):
    await ctx.send(embed=cr.emb(cr.green, "Loaded Cogs", '   ✅\n\n'.join(loaded_cog_list) + "  ✅\n"))
    if not unloaded_cog_list == []:
        await ctx.send(embed=cr.emb(cr.red, "Unloaded Cogs", '  ❌\n\n'.join(unloaded_cog_list) +"  ❌\n"))

@commands.is_owner()
@client.slash_command(description="Load Cogs",guild_ids=[1003683013625925664])
async def load(ctx, name:str=commands.Param(choices=unloaded_cog_list)):
    client.load_extension(f'Cogs.{name}')
    unloaded_cog_list.remove(name)
    loaded_cog_list.append(name)

    await ctx.send(embed=cr.emb(cr.green, "Loaded", f"{name} function"))

@commands.is_owner()
@client.slash_command(description="Reload Cogs",guild_ids=[1003683013625925664])
async def reload(ctx:disnake.ApplicationCommandInteraction, name:str=commands.Param(choices=loaded_cog_list)):
    # print(loaded_cog_list)
    client.unload_extension(f'Cogs.{name}')
    loaded_cog_list.remove(name)
    unloaded_cog_list.append(name)
    client.load_extension(f'Cogs.{name}')
    unloaded_cog_list.remove(name)
    loaded_cog_list.append(name)
    await ctx.send(embed=cr.emb(cr.green, "Reloaded", f"{name} function"))

      

@commands.is_owner()
@client.slash_command(description="Unloads Cogs",guild_ids=[1003683013625925664])
async def unload(ctx, name:str=commands.Param(choices=loaded_cog_list)):
    client.unload_extension(f'Cogs.{name}')
    loaded_cog_list.remove(name)
    unloaded_cog_list.append(name)
    await ctx.send(embed=cr.emb(cr.red, "Unloaded", f"{name} function"))

try:
  client.loop.run_until_complete(client.start(os.getenv("Mr_Robot")))
except Exception as e:
  print(f"Login Failure at {datetime.datetime.now()}")
finally:
  client.loop.close()
