# MODULES IMPORT

import datetime
import time
from webserver import keep_alive
import requests as req
import os
import disnake
from disnake.client import Client
from disnake.ext import tasks, commands
import praw
import asyncio
import random

# VARIABLE INIT

start_time = time.time()

client = commands.Bot(command_prefix=commands.when_mentioned_or('!!'),intents = disnake.Intents.all())

reddit = praw.Reddit(client_id='gn-1O5327M3caeYY25qBIg',
                     client_secret='fNu5KPbonvUa6H-KqGD1nouGpYMfUA',
                     user_agent='MR ROBOT meme',
                     timeout=60)

# EVENTS


class cr:
    red = 0xff0000
    green = 0x00ff00
    blue = 0x0000ff
    black = 0x000000
    orange =0xffa500

    def emb(color=green, name='', value=''):
        Em = disnake.Embed(color=color, title=name, description=value)
        Em.timestamp = datetime.datetime.utcnow()
        Em.set_footer(text="MR ROBOT", icon_url="https://img1.pnghut.com/t/5/0/13/LQ7V4wPn14/facial-hair-mr-robot-kali-linux-tshirt-brand.jpg")
        return Em

# def cr.emb(color=green, name='', value=''):
#     Em = disnake.Embed(color=color, title=name, description=value)
#     Em.set_footer(text="MR ROBOT")
#     return Em


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
    os.system('kill 1')
except Exception as error:
    with open('Logs/error.log','a') as file:
      file.write(f'\nEXITING: {error}')
    os.system('kill 1')
