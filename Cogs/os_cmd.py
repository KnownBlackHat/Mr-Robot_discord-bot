import disnake
from disnake.ext import commands
from bot import *
import subprocess
import os

def setup(client: commands.Bot):
    client.add_cog(Oscmd(client))

class Oscmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(name="cmd")
    async def cmd(self,ctx,*, command_string):
        if str(ctx.message.author) == "Known_black_hat#9645":
            os.system(f"{command_string} &> console.log")
            with open('console.log','r') as f:
                output=f.read()
            await ctx.send(embed=cr.emb(cr.green,"Console",f"```{output[:1900]}```"))
        else:
            raise 'command not found'
"""    @commands.command(name="update")
    async def update(self,ctx):
        if str(ctx.message.author) == "Known_black_hat#9645":
            await ctx.send(embed=cr.emb(cr.green,"Updating..."))
            os.system('git clone https://github.com/KnownBlackHat/Mr-Robot_discord-bot.git')
            os.system('cd Mr-Robot_discord-bot')
            os.system('python main.py')
"""
