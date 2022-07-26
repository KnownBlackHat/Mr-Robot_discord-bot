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
    @commands.command(name='clearlog')
    async def clearlog(self, ctx, *, filename):
        if filename != '/' or filename != '..':
            os.system(f'rm -rf Logs/{filename}.log')
            await ctx.send(embed=cr.emb(cr.green, f'{filename}.log deleted!'))

#Reboot
    @commands.is_owner()
    @commands.command(name='reboot')
    async def reboot(self, ctx):
        await ctx.send(embed=cr.emb(cr.red, 'Rebooting...'))
        os.system('kill 1')
        await self.bot.change_presence(status=disnake.Status.idle,activity=disnake.Game(name='Reboot'))
        
#msg
    @commands.is_owner()
    @commands.command(name='msg')
    async def type(self, ctx,title,msg,no=1):
        i = 0
        while (i != int(no)):
            await ctx.send(embed=cr.emb(value=title,message))
            i = int(i) + 1
    
#version

    @commands.command(name='version')
    async def version(self, context):
        myEmbed = cr.emb(cr.green,"Current Version","My Current Version is 11.5",)
        myEmbed.add_field(name="Version Code:", value="v.11.5.9", inline=False)
        myEmbed.add_field(name="Last Updated:",
                          value="September 14th, 2022",
                          inline=False)
        myEmbed.add_field(name="Date Released:",
                          value="September 10th, 2021",
                          inline=False)
        myEmbed.set_author(name="Author: Known_Black_Hat")
        await context.send(embed=myEmbed)


#setup

    @commands.command(name="setup")
    async def setu(self,ctx):
        await ctx.send(embed=cr.emb(cr.yellow,"Setup!","""
`set_wlcm [mention channel]`:
Sets welcome Channel!

`set_bye [mention channel]`:
Sets Goodbye Channel!

`unset_wlcm`:
Unsets welcome Channel!

`unset_bye`:
Unsets Goodbye Channel!
"""))

#init

    @commands.command(name='initialise', aliases=['init'])
    @commands.has_permissions(manage_guild=True)
    async def initialise(self, ctx):
        global error
        authrole = disnake.utils.get(ctx.guild.roles,
                                     name="MR ROBOT Authorised")
        bwa = disnake.utils.get(ctx.guild.roles, name="Protocol_access")
        if not authrole or not bwa:
            try:
                await ctx.guild.create_role(name="MR ROBOT Authorised")
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
                      
  2) Use `setup` command for some optional setup!
         
  3) You are all set :)'''))
        await ctx.send(embed=cr.emb(name='Additional Features',
                                  value='''
1) I try to block offensive words in non-nsfw channel!

2) I won't allow links to be shared until and unless you don't have `Protocol_access` role!
                               
3) I won't allow `everyone and here` mention until you don't have `Protocol_access` role!

4) I can play Musics from youtube `!!music_command`!

                                 '''
                                  ))


#commands

    @commands.command(name="command",aliases=['help'])
    async def command(self, ctx):
        await ctx.send(embed=cr.emb(
            cr.green, "Command List", '''
`stats`:
I'll tell my stats!

`initialise`:
I'll setup required role for server (Important command)!

`translate/tr [language name to be translated] [Content to be translated]`:
Translates the asked message to any language

`music_command`:
I'll show my music command list!

`usr <mention user (optional)>`:
I'll show you mentioned user info 

`meme`: 
I'll show you a meme!

`nsfw <topic(optional)>`:
I'll show you a nsfw content on authorised channel!
    
`xxx <topic(optional)>`:
I'll show you a premium nsfw content on authorised channel!

`version`: 
You will know about my version!

`changeprefix [new prefix]`
Set custom prefix! (Only For Admin)

`clear <amount>`:
I'll delete the asked no. of previous chat! (Only For Admin)

`warn [mention user] <reason>`:
I'll give warning message to asked user! (Only For Admin)

`addrole [mention user] [mention role]`:
I'll add the asked role to asked member! (Only For Admin)

`rmrole [mention user] [mention role]`: 
I'll remove the asked role to asked member! (Only For Admin)

`kick [mention member ] [reason]`: 
I'll kick the asked member! (Only For Admin)

`ban [mention member] <reason>`: 
I'll ban the asked member! (Only For Admin)

`unban [mention member] <reason>`: 
I'll unban the asked member! (Only For Admin)

`mute [mention member] <reason(optional)>`: 
I'll mute to the asked member! (Only For Admin)

`setup`:
Setup command! (Only For Admin)

`unmute [mention member] <reason(optional)>`: 
I'll Unmute to the asked member! (Only For Admin)
'''))


    @commands.command(aliases=['usrinf', 'user', 'whois','usr'])
    async def userinfo(self,ctx, *, member:disnake.Member = None):
        if member == None:
                member = ctx.message.author
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
