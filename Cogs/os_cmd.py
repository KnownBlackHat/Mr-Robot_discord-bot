import disnake
from disnake.ext import commands
from bot import cr
import subprocess
import os

def setup(client: commands.Bot):
    client.add_cog(Oscmd(client))

class Oscmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.is_owner() 
    @commands.slash_command(name="cmd",description="Runs Console Commands")
    async def cmd(self,ctx,*, command_string):
        output = subprocess.getoutput(command_string)
        await ctx.send(embed=cr.emb(cr.green,"Console",f"```\n{output[:1900]}\n```"))
        

    @commands.is_owner()
    @commands.slash_command(name="update",description="Updates the software from github")
    async def update(self,ctx):
        await self.bot.change_presence(status=disnake.Status.idle,activity=disnake.Game(name='Update'))
        await ctx.send(embed=cr.emb(cr.green,"Updating..."))
        os.system("rm -rf Mr*")
        os.system('git clone https://github.com/KnownBlackHat/Mr-Robot_discord-bot.git')
        for i in os.listdir():
            if i == "Mr-Robot_discord-bot":
                ...
            elif i == "greeting_channel.json":
                ...
            elif i == "poetry.lock":
                ...
            elif i == "pyproject.toml":
                ...
            elif i == ".env":
                ...
            else:
#                    await ctx.send(i)
                os.system(f'rm -rf {i}')
        os.system("rm -rf Mr*/greeting_channel.json Mr*/pyproject.toml Mr*/poetry.lock")
        os.system("mv Mr*/* .")
#             os.system("rm -rf requirements.txt")
        await ctx.send(embed=cr.emb(cr.green,"Update Completed"))
        os.system("python main.py")
