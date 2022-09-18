import disnake
from disnake.ext import commands
from bot import cr
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
            member_channel = None
        if member_channel is not None:
            try:
                embed=cr.emb(disnake.Colour.random(),f'Welcome {member.name}!')
                try:
                    embed.set_thumbnail(url=member.avatar.url)
                except Exception:
                    embed.set_thumbnail(url="https://cdn.logojoy.com/wp-content/uploads/20210422095037/discord-mascot.png")
                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
                await member_channel.send(embed=embed)
            except Exception as e:
                ...



    # @commands.slash_command(name='set_wlcm',description="Sets welcoming message channel of server")
    # @commands.default_member_permissions(manage_guild = True)
    # async def set_wlcm(self,ctx,channel: disnake.TextChannel):
    #     with open('greeting_channel.json','r') as file:
    #             greet_channel=json.load(file)
    #     greet_channel[str(ctx.guild.id)]["greet_channel"] = str(channel.id)
    #     json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
    #     await ctx.send(embed=cr.emb(cr.green,"Welcome Channel Set Sucessfully",f"Channel: {channel}"))

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        try:
            member_channel= self.bot.get_channel(int(greet_channel[str(member.guild.id)]["goodbye_channel"]))
        except Exception as e:
            member_channel = None
        if member_channel is not None:
            try:
                embed=cr.emb(disnake.Colour.random(),f'Goodbye {member.name}!')
                try:
                    embed.set_thumbnail(url=member.avatar.url)
                except Exception:
                    embed.set_thumbnail(url="https://cdn.logojoy.com/wp-content/uploads/20210422095037/discord-mascot.png")
                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"), inline=False)
                await member_channel.send(embed=embed)
            except Exception as e:
                ...

    @commands.slash_command(name='set',description="Set's the features of channel in the server")
    @commands.default_member_permissions(manage_guild = True)
    async def set(self,ctx,channel: disnake.TextChannel,feature:str = commands.Param(choices=["Welcome Channel","Goodbye Channel"])):
        if feature == "Welcome Channel":
            with open('greeting_channel.json','r') as file:
                greet_channel=json.load(file)
            greet_channel[str(ctx.guild.id)]["greet_channel"] = str(channel.id)
            json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.green,"Welcome Channel Set Sucessfully",f"Channel: {channel}"))
        elif feature == "Goodbye Channel":
            with open('greeting_channel.json','r') as file:
                greet_channel=json.load(file)
            greet_channel[str(ctx.guild.id)]["goodbye_channel"] = str(channel.id)
            json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.green,"Goodbye Channel Set Sucessfully",f"Channel: {channel}"))

    # @commands.slash_command(name='set_bye',description="Sets bye message channel of server")
    # @commands.default_member_permissions(manage_guild = True)
    # async def set_bye(self,ctx,channel: disnake.TextChannel):
    #     with open('greeting_channel.json','r') as file:
    #             greet_channel=json.load(file)
    #     greet_channel[str(ctx.guild.id)]["goodbye_channel"] = str(channel.id)
    #     json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
    #     await ctx.send(embed=cr.emb(cr.green,"Goodbye Channel Set Sucessfully",f"Channel: {channel}"))


    @commands.slash_command(name='unset',description="Unset's the features of channel in the server")
    @commands.default_member_permissions(manage_guild = True)
    async def unset(self,ctx,channel: disnake.TextChannel,feature:str = commands.Param(choices=["Welcome Channel","Goodbye Channel"])):
        if feature == "Welcome Channel":
            with open('greeting_channel.json','r') as file:
                greet_channel=json.load(file)
            greet_channel[str(ctx.guild.id)]["greet_channel"] = None
            json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.red,"Welcome Channel Unset Sucessfully"))
        elif feature == "Goodbye Channel":
            with open('greeting_channel.json','r') as file:
                greet_channel=json.load(file)
            greet_channel[str(ctx.guild.id)]["goodbye_channel"] = None
            json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.red,"Goodbye Channel Unset Sucessfully"))

    # @commands.slash_command(name='unset_wlcm',description="Unsets welcoming message channel of server")
    # @commands.default_member_permissions(manage_guild = True)
    # async def unset_wlcm(self,ctx):
    #     with open('greeting_channel.json','r') as file:
    #             greet_channel=json.load(file)
    #     greet_channel[str(ctx.guild.id)]["greet_channel"] = None
    #     json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
    #     await ctx.send(embed=cr.emb(cr.green,"Welcome Channel Unset Sucessfully"))
