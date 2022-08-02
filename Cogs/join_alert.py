import disnake
from disnake.ext import commands
from bot import *

def setup(client: commands.Bot):
    client.add_cog(Joinalert(client))

class Joinalert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = client.get_channel(1003683383324455043)
        print (channel)
        #link = client.create_invite(destination=guild,xkcd=True,max_age=0,max_uses=number)
        await channel.send(embed=cr.emb(disnake.Colour.random(),"Joined",f"""
Name: {guild.name}
Id: {guild.id}
"""))
