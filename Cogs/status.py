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
