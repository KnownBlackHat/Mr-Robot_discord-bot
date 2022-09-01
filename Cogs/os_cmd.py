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
            await self.bot.change_presence(status=disnake.Status.idle,activity=disnake.Game(name='Update'))
            await ctx.send(embed=cr.emb(cr.green,"Updating..."))
            os.system("rm -rf Mr*")
            os.system('git clone https://github.com/KnownBlackHat/Mr-Robot_discord-bot.git')
            for i in os.listdir():
                if i == "Mr-Robot_discord-bot":
                    ...
                elif i == "greeting_channel.json":
                    ...
                else:
#                    await ctx.send(i)
                    os.system(f'rm -rf {i}')
            os.system("rm -rf Mr*/greeting_channel.json")
            os.system("mv Mr*/* .")
            await ctx.send(embed=cr.emb(cr.green,"Update Completed"))
            os.system("python main.py")
