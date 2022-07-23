import psutil
from asyncio import FastChildWatcher
import disnake
from disnake.ext import commands
from main import *


def setup(client: commands.Bot):
    client.add_cog(command_handling(client))


class command_handling(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        os.system('clear')
        print(f'\n[!] Bot name: {client.user} Id: {client.user.id} \n')
        os.system('curl -s ifconfig.me >>ip.txt ; echo '' >> ip.txt')
        guild_count = 0
        with open('Server_Status.inf','w') as f:
          f.write(f'\n[!] Bot name: {client.user} Id: {client.user.id} \n')
          for guild in self.bot.guilds:
            f.write(f"\n[-] {guild.id} (Name: {guild.name})")
            guild_count = guild_count +1
          f.write(f"\n\n[=] {client.user} is in " + str(guild_count) + " guilds.")

        await self.bot.change_presence(status=disnake.Status.idle,
                                       activity=disnake.Game(name='!!command'))



    @commands.command(name="stats")
    async def status(self,ctx):
      current_time = time.time()
      difference = int(round(current_time - start_time))
      text = str(datetime.timedelta(seconds=difference))
      embed=cr.emb(cr.green,"Status")
      embed.add_field("Ping: ",f"{round(client.latency * 1000)}ms",False)
      embed.add_field("Uptime: ",f"{text}",False)
      embed.add_field("Cpu Usage: ",f"{psutil.cpu_percent()}%",False)
      embed.add_field("Memory Usage: ",f"{psutil.virtual_memory().percent}%",False)
      embed.add_field("Available Usage: ",f"{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%",False)
      embed.add_field("Users: ", ctx.guild.member_count, False)
      embed.add_field("Channels: ", len(ctx.guild.channels),False)