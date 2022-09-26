import disnake
from disnake.ext import commands
from bot import cr
import os

def setup(client: commands.Bot):
    client.add_cog(misc(client))


class misc(commands.Cog):
    def __init__(self, client):
        self.bot = client

#Clearlog
    @commands.is_owner()
    @commands.slash_command(name='clearlog',description="Delete the logs",guild_ids=[1003683013625925664])
    async def clearlog(self, ctx, *, filename):
        if filename != '/' or filename != '..':
            os.system(f'rm -rf Logs/{filename}.log')
            await ctx.send(embed=cr.emb(cr.green, f'{filename}.log deleted!'))

#Reboot
    @commands.is_owner()
    @commands.slash_command(name='shutdown',description="Shutdown command",guild_ids=[1003683013625925664])
    async def reboot(self, ctx):
        await ctx.send(embed=cr.emb(cr.red, 'Shutting Down...'))
        await self.bot.change_presence(status=disnake.Status.idle,activity=disnake.Game(name='ShutDown'))
        exit()
        
#message
    @commands.is_owner()
    @commands.command(name='embed')
    async def type(self, ctx,colour=cr.green,title,message):
            await ctx.send(embed=cr.emb(colour,title,message))
    @type.error
    async def type_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Missing argument: {error.param.name}!")

    @commands.default_member_permissions(manage_guild=True)
    @commands.slash_command(name='message',description="Send custom message from my side in server")
    async def type(self,ctx,message, amount=1):
        no = amount
        i = 0
        await ctx.send(embed=cr.emb(cr.green,"Message sent"),ephemeral=True)
        while (i != int(no)):
            await ctx.send(embed=cr.emb(cr.green,message))
            i = int(i) + 1
    
#version

    @commands.slash_command(name='version',description="Shows my version")
    async def version(self, context):
        myEmbed = cr.emb(cr.green,"Current Version","My Current Version is 14.8",)
        myEmbed.add_field(name="Version Code:", value="v.14.8.2", inline=False)
        myEmbed.add_field(name="Last Updated:",
                          value="September 18th, 2022",
                          inline=False)
        myEmbed.add_field(name="Date Released:",
                          value="September 10th, 2021",
                          inline=False)
        myEmbed.set_author(name="Author: Known_Black_Hat")
        await context.send(embed=myEmbed)


# #setup

#     @commands.slash_command(name="setup",description="Setup command for server")
#     async def setu(self,ctx):
#         await ctx.send(embed=cr.emb(cr.yellow,"Setup!","""
# `set_wlcm [mention channel]`:
# Sets welcome Channel!

# `set_bye [mention channel]`:
# Sets Goodbye Channel!

# `unset_wlcm`:
# Unsets welcome Channel!

# `unset_bye`:
# Unsets Goodbye Channel!
# """))

#init

    @commands.slash_command(name='initialise',description="Initialises server (Important for first time setup)")
    @commands.default_member_permissions(manage_guild=True)
    async def initialise(self, ctx):
        global error
        authrole = disnake.utils.get(ctx.guild.roles, name="Protocol_access")
        if not authrole:
            try:
                await ctx.guild.create_role(name="Protocol_access")
                await ctx.send(embed=cr.emb(cr.green, "!!DONE!!",
                                          "Successfully initialised!"))

            except Exception as error:
                await ctx.send(embed=cr.emb(cr.red, "!!Error!!", f": {error}"))
        else:
            await ctx.send(
                embed=cr.emb(cr.green, "!^_^!", "Already initialised!"))
        await ctx.send(embed=cr.emb(
            name="Perform the following actions to complete initialisation!",
            value=
            '''
                               
  1) Assign `Protocol_access` role in order to share link in the server!
                               
  2) [Optional] Use `/manage_feature`,`/set`,`/unset` command for more customisation!'''))


#commands

    @commands.slash_command(name="help",description="Shows Command List")
    async def command(self, ctx):
        await ctx.send(embed=cr.emb(
            cr.green, "Command List", '''
`status`:
I'll tell my status!

`manage_feature`:
You can toggle between activate/deactivate my features!

`initialise`:
I'll setup required role for server (Important command)!

`translate`:
Translates the asked message to any language

`music_command`:
I'll show my music command list!

`userinfo`:
I'll show you mentioned user info 

`meme`: 
I'll show you a meme!

`nsfw`:
I'll show you a nsfw content on authorised channel!
    
`xxx`:
I'll show you a premium nsfw content on authorised channel!

`version`: 
You will know about my version!

`clear`:
I'll delete the asked no. of previous chat! (Only For Admin)

`warn`:
I'll give warning message to asked user! (Only For Admin)

`addrole`:
I'll add the asked role to asked member! (Only For Admin)

`rmrole`: 
I'll remove the asked role to asked member! (Only For Admin)

`kick`: 
I'll kick the asked member! (Only For Admin)

`ban`: 
I'll ban the asked member! (Only For Admin)

`unban`: 
I'll unban the asked member! (Only For Admin)

`mute`: 
I'll mute to the asked member! (Only For Admin)

`set`|`unset`:
Set/unset command for welcome/goodbye!


`unmute`: 
I'll Unmute to the asked member! (Only For Admin)
 '''))


    @commands.slash_command(name="userinfo",description="Shows User Info")
    async def userinfo(self,ctx, *, member:disnake.Member = None):
        if member == None:
                member = ctx.author
        try:
            embed=cr.emb(member.color,f"{member} Information")
            try:
                embed.set_thumbnail(url=member.avatar.url)
            except Exception:
                embed.set_thumbnail(url="https://cdn.logojoy.com/wp-content/uploads/20210422095037/discord-mascot.png")
            embed.add_field(name="Name", value=member.name,inline=False)
            embed.add_field(name="Nickname", value=member.nick,inline=False)
            embed.add_field(name="ID", value=member.id,inline=False)
            embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"),inline=False)
            embed.add_field(name="Joined",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"),inline=False)
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            embed.add_field(name="Join Position", value=str(members.index(member)+1),inline=False)
            embed.add_field(name="Status", value=member.status,inline=False)
            embed.add_field(name='Activity: ', value=member.activity,inline=False)
            embed.add_field(name='Highest Role', value=member.top_role,inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(embed=cr.emb(cr.red,'User Info Error', f"Error: {e}"))
