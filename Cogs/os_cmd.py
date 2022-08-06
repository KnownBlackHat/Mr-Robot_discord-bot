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
            output = subprocess.getoutput(command_string)
            await ctx.send(embed=cr.emb(cr.green,"Console",f"```\n{output[:1900]}\n```"))
        else:
            raise 'Command not found'



    @commands.command(name="update")
    async def update(self,ctx):
        if str(ctx.message.author) == "Known_black_hat#9645":
            await ctx.send(embed=cr.emb(cr.green,"Updating..."))
            os.system("rm -rf Mr_Robot-discord_bot")
            os.system('git clone https://github.com/KnownBlackHat/Mr-Robot_discord-bot.git')
            os.system('cd Mr-Robot_discord-bot')
            for i in os.listdir():
                if i == "Mr_Robot-discord_bot":
                    ...
                elif i == "greeting_channel.json":
                    ...
                else:
                    await ctx.send(i)
                    os.system(f'rm -rf {i}')
            os.system("mv Mr_Robot-discord_bot/* .")
            await ctx.send(embed=cr.emb(cr.green,"Update Completed","I will be back in few minutes"))
            os.system("python main.py")
