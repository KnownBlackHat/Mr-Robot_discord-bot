import disnake
from disnake.ext import commands
from bot import *
import json
def setup(client: commands.Bot):
    client.add_cog(Greetings(client))

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        try:
            member_channel= self.bot.get_channel(int(greet_channel[str(member.guild.id)]["greet_channel"]))
        except Exception as e:
#            print(e)
            member_channel = member.guild.system_channel
#        print(member_channel)
        if member_channel is not None:
            try:
                embed=cr.emb(disnake.Colour.random(),f'Welcome {member.name}')
                try:
                    embed.set_thumbnail(url=member.avatar.url)
                except Exception:
                    embed.set_thumbnail(url="https://cdn.logojoy.com/wp-content/uploads/20210422095037/discord-mascot.png")
                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
                await member_channel.send(embed=embed)
            except Exception as e:
                ...
    @commands.command(name='set_wlcm')
    @commands.has_any_role("MR ROBOT Authorised")
    async def set_wlcm(self,ctx,channel: disnake.TextChannel):
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        greet_channel[str(ctx.guild.id)]["greet_channel"] = str(channel.id)
        json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
        await ctx.send(embed=cr.emb(cr.green,"Welcome Channel Set Sucessfully",f"Channel: {channel}"))
