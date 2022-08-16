# MODULE INSTALLATION
import os
#os.system("pip install -r requirements.txt")
# MODULES IMPORT
import requests as r
import datetime
import time
from webserver import keep_alive
import disnake
from disnake.client import Client
from disnake.ext import tasks, commands
import asyncio
import random
from dotenv import load_dotenv
import json
# VARIABLE INIT

start_time = time.time()
def get_prefix(client,message):
    with open('greeting_channel.json','r') as file:
        prefixes=json.load(file)
    try:
        prefixes[str(message.guild.id)]["prefix"]
    except:
        prefixes[str(message.guild.id)]["prefix"] = "!!"
        json.dump(prefixes,open('greeting_channel.json','w'),indent=2)
    return commands.when_mentioned_or(prefixes[str(message.guild.id)]["prefix"])(client,message)


client = commands.Bot(command_prefix=get_prefix, intents = disnake.Intents.all())

load_dotenv()

# EVENTS


class cr:
    red = 0xff0000
    green = 0x00ff00
    blue = 0x0000ff
    black = 0x000000
    orange = 0xffa500
    yellow = 0xffff00

    def emb(color=green, name='', value=''):
        Em = disnake.Embed(color=color, title=name, description=value)
        Em.timestamp = datetime.datetime.utcnow()
        Em.set_footer(text="MR ROBOT", icon_url="https://www.logolynx.com/images/logolynx/17/17688231e794e005ef6511061bd9f1c0.jpeg")
        return Em


@client.remove_command('help')
@client.command(name='list_cogs')
async def list_functions(ctx):
    await ctx.send(embed=cr.emb(cr.green, "Loaded Cogs", '   ✅\n\n'.join(loaded_cog_list) + "  ✅\n"))
    if not unloaded_cog_list == []:
        await ctx.send(embed=cr.emb(cr.red, "Unloaded Cogs", '  ❌\n\n'.join(unloaded_cog_list) +"  ❌\n"))


@client.command(name='load')
async def load(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
        client.load_extension(f'Cogs.{name}')
        try:
            unloaded_cog_list.remove(name)
            loaded_cog_list.append(name)
        except Exception:
            ...
        await ctx.send(embed=cr.emb(cr.green, "Loaded", f"{name} function"))

@client.command(name='reload')
async def reload(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
      client.unload_extension(f'Cogs.{name}')
      client.load_extension(f'Cogs.{name}')
      await ctx.send(embed=cr.emb(cr.green, "Reloaded", f"{name} function"))

      
@client.command(name='unload')
async def unload(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
        client.unload_extension(f'Cogs.{name}')
        try:
            loaded_cog_list.remove(name)
            unloaded_cog_list.append(name)
        except Exception:
            ...
        await ctx.send(embed=cr.emb(cr.red, "Unloaded", f"{name} function"))


error = ''
unloaded_cog_list=[]
loaded_cog_list= []
try:
    for file in os.listdir('Cogs'):
        if file.endswith('.py'):
            try:
                client.load_extension(f'Cogs.{str(file[:-3])}')
                loaded_cog_list.append(file[:-3])
            except Exception as e:
                unloaded_cog_list.append(file[:-3])

except Exception as error:
    with open('Logs/error.log','a') as file:
      file.write(f'\nCogs Error: {error}')

keep_alive()
try:
    client.run(str(os.getenv('TOKEN')))
    os.system("kill 1")
except:
    os.system("kill 1")
