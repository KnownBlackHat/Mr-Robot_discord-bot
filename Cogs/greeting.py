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
                try:
                    embed.set_thumbnail(url=member.avatar.url)
                except Exception:
                    embed.set_thumbnail(url="data:image/png;base64,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")
                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
                await ctx.send(embed=embed)
            except Exception as e:
                ...
