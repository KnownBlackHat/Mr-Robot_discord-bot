import disnake
from disnake.ext import commands
from bot import cr,client
import json

def setup(client: commands.Bot):
    client.add_cog(Joinalert(client))

class Joinalert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = client.get_channel(1003683383324455043)
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        greet_channel[guild.id] = {}
        greet_channel[guild.id]["name"] = guild.name
        greet_channel[guild.id]["prefix"] = "!!"
        json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
        #link = client.create_invite(destination=guild,xkcd=True,max_age=0,max_uses=number)
        await channel.send(embed=cr.emb(disnake.Colour.random(),"Joined",f"""
Name: {guild.name}
Id: {guild.id}
"""))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        greet_channel.pop(str(guild.id))
        json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
