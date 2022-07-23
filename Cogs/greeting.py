import disnake
from disnake.ext import commands
from main import *

def setup(client: commands.Bot):
    client.add_cog(Greetings(client))

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ctx = member.guild.system_channel
        if ctx is not None:
            try:
                embed=cr.emb(disnake.Colour.random(),f'Welcome {member.name}')
                embed.set_thumbnail(url=member.avatar.url, inline=False)
                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC", inline=False))
                await ctx.send(embed=embed)
            except Exception as e:
                ...