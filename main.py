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


def emb(color=cr.green, name='', value=''):
    Em = disnake.Embed(color=color, title=name, description=value)
    Em.set_footer(text="MR ROBOT")
    return Em


@client.remove_command('help')
@client.command(name='list_functions')
async def list_functions(ctx):
    await ctx.send(
        embed=emb(cr.green, "Available Functions", ', '.join(function_list)))


@client.command(name='load')
async def load(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
        client.load_extension(f'Cogs.{name}')
        await ctx.send(embed=emb(cr.green, "Loaded", f"{name} function"))

@client.command(name='reload')
async def reload(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
      client.unload_extension(f'Cogs.{name}')
      client.load_extension(f'Cogs.{name}')
      await ctx.send(embed=emb(cr.green, "Reloaded", f"{name} function"))

      
@client.command(name='unload')
async def unload(ctx, name):
    if str(ctx.message.author) == "Known_black_hat#9645":
        client.unload_extension(f'Cogs.{name}')
        await ctx.send(embed=emb(cr.red, "Unloaded", f"{name} function"))


error = ''

function_list = []
try:
    for file in os.listdir('Cogs'):
        if file.endswith('.py'):
            function_list.append(file[:-3])
            client.load_extension(f'Cogs.{str(file[:-3])}')
except Exception as error:
    with open('Logs/error.log','a') as file:
      file.write(f'\nCogs Error: {error}\n')

keep_alive()
try:
    client.run(str(os.getenv('TOKEN')))
    os.system('kill 1')
except Exception as error:
    with open('Logs/error.log','a') as file:
      file.write(f'\nEXITING: {error}\n')
    os.system('kill 1')
