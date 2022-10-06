import disnake
from disnake.ext import commands
import datetime
from bot import cr
import json

MISSING="MISSING"

def setup(client: commands.Bot):
    client.add_cog(moderation(client))


class moderation(commands.Cog):
    def __init__(self, client):
        self.bot = client

    
#add and remove feature
    @commands.slash_command(name='manage_features',description="Toggles my features in server")
    @commands.default_member_permissions(manage_guild = True)
    async def manage_features(self,ctx,option:str = commands.Param(choices=["Activate","Deactivate"]),feature:str = commands.Param(choices=["Link Blocker","Anti-Abusive","@everyone/@here mention blocker"])):
        with open('greeting_channel.json','r') as file:
                feature_db=json.load(file)
        if option == "Activate":
            feature_db[str(ctx.guild.id)][feature] = 'activate'
            json.dump(feature_db,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.green,"Activated",feature))
        elif option == "Deactivate":
            feature_db[str(ctx.guild.id)][feature] = 'deactivate'
            json.dump(feature_db,open('greeting_channel.json','w'),indent=2)
            await ctx.send(embed=cr.emb(cr.red,"Deactivated",feature))

#clear

    @commands.slash_command(name='clear',description="Deletes the messages")
    @commands.default_member_permissions(manage_messages=True)
    async def clear(self, context, amount=1):
        await context.send(embed=cr.emb(cr.yellow,"Deleting Message..."),ephemeral=True)
        await context.channel.purge(limit=int(amount))

    # @commands.slash_command(name='changeprefix')
    # @commands.default_member_permissions(manage_guild=True)
    # async def changeprefix(self, ctx, *,prefix):
    #     with open('greeting_channel.json','r') as file:
    #             prefixes=json.load(file)
    #     if prefix.startswith('"') and prefix.endswith('"'):
    #         prefix = prefix.replace('"','')
    #     elif prefix.startswith("'") and prefix.endswith("'"):
    #         prefix = prefix.replace("'","")
    #     prefixes[str(ctx.guild.id)]["prefix"] = prefix
    #     json.dump(prefixes,open('greeting_channel.json','w'),indent=2)
    #     await ctx.send(embed=cr.emb(cr.green,"New Server Prefix",f'`{prefix}`'))

    @commands.slash_command(name='addrole',description="Adds the roles")
    @commands.default_member_permissions(manage_roles=True)
    async def addrole(self, ctx, user: disnake.Member, role: disnake.Role):
        role = disnake.utils.get(user.guild.roles, name=str(role))
        await user.add_roles(role)
        await ctx.send(embed=cr.emb(cr.green, "Role Assigned",
                                  f"{user.mention} Has Got  `{role}`  Role !"), delete_after=10)
        try:
            await user.send(
                embed=cr.emb(cr.green, "Role Assigned",
                          f" You got `{role}` Role In {ctx.guild.name} !"))
        except:
            ...

    @commands.slash_command(name='rmrole',description="Removes the roles")
    @commands.default_member_permissions(manage_roles=True)
    async def rmrole(self, ctx, user: disnake.Member, role: disnake.Role):
        role = disnake.utils.get(user.guild.roles, name=str(role))
        await user.remove_roles(role)
        await ctx.send(
            embed=cr.emb(cr.red, "Role Removed",
                      f"{user.mention} Was Removed  `{role}` Role !"), delete_after= 10)
        try:
            await user.send(embed=cr.emb(
                cr.red, "Role Removed",
                f"You got removed from `{role}` Role In {ctx.guild.name}!"))
        except:
            ...

    @commands.slash_command(name='unban',description="Unbans the member")
    @commands.default_member_permissions(ban_members=True)
    async def unban(self, context, member):
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await context.guild.unban(user)
                await context.send(
                    embed=cr.emb(cr.green,"Unbanned",f'Unbanned: {user}'),delete_after=10)
                try:
                    await member.send(embed=cr.emb(
                        name=
                        f'You Were Unbanned From The {context.guild.name} Server!'
                    ))
                except:
                    pass

                return

    @commands.slash_command(name='ban',description="Bans the member")
    @commands.default_member_permissions(ban_members=True)
    async def ban(self, context, member: disnake.Member, *, reason=None):
        try:
            await member.send(embed=cr.emb(cr.red,f'You Were Banned From The {context.guild.name} Server!',f'Reason: {reason}'),delete_after=10)
        except:
            pass
        await member.ban(reason=reason)
        await context.send(embed=cr.emb(cr.red,"Banned",f'Banned: {member} Reason: {reason}'))

    @commands.slash_command(name="temporary_mute",description="Temporarily mutes the member")
    @commands.default_member_permissions(moderate_members=True)
    async def edit(self,ctx,member: disnake.Member,hours:int,days:int =0,reason:str="None"):
        if days == 0 and hours == 0:
            await ctx.send(embed=cr.emb(cr.red,"Error","User can't be muted for 0 minutes"),ephemeral=True)
        else:
            await member.edit(timeout=datetime.timedelta(days=days,hours=hours).seconds)
            await member.send(embed=cr.emb(cr.red,f"You are Temporarily Muted in the {ctx.guild.name} server",f"Reason: {reason}"))
            await ctx.send(embed=cr.emb(cr.red,"Temporarily Muted",f"{member.mention} is muted For {datetime.timedelta(days=days,hours=hours)}"),ephemeral=True)
#         until: Optional[datetime.datetime] = MISSING,
#         reason: Optional[str] = None,
#     ) -> Member:
#         if duration is not MISSING:
#             return await self.guild.timeout(self, duration=duration, reason=reason)
#         else:
#             return await self.guild.timeout(self, until=until, reason=reason)
    @commands.slash_command(name="mute",description="Mutes the member")
    @commands.default_member_permissions(moderate_members=True)
    async def mute(self, ctx, member: disnake.Member,reason=None):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole,
                                              speak=False,
                                              send_messages=False,
                                              read_message_history=True,
                                              read_messages=True,
                                              view_channel=True)

        await member.add_roles(mutedRole)
        await ctx.send(embed=cr.emb(
            cr.red,"Muted",f" Muted: {member.mention} Reason: {reason}"),delete_after=10)
        await member.send(embed=cr.emb(
            cr.red,
            f"You are Muted in the {guild.name} server",f"Reason: {reason}"))

    @commands.slash_command(name="unmute",description="Unmute the member")
    @commands.default_member_permissions(moderate_members=True)
    async def unmute(self, ctx, member: disnake.Member):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await ctx.send(
            embed=cr.emb(cr.green,"Unmuted",f"Unmuted {member.mention}"),delete_after=10)
        await member.send(embed=cr.emb(cr.green,
            f"You are Unmuted in the {guild.name} server!"," 😉😉Enjoy😉😉!"))

    @commands.slash_command(name='kick',description="Kicks the member")
    @commands.default_member_permissions(kick_members=True)
    async def kick(self, context, member: disnake.Member, *, reason=None):
        try:
            await member.send(embed=cr.emb(
                cr.red,
                f'You Were Kicked From The {context.guild.name} Server! ',f'Reason: {reason}'
            ))
        except:
            pass
        await member.kick(reason=reason)
        await context.send(
            embed=cr.emb(cr.red,"Kicked",f'Kicked: {member} Reason: {reason}'))

    @commands.slash_command(name="dm",description="Dm's the user")
    @commands.default_member_permissions(moderate_members=True)
    async def dm(self, ctx, member: disnake.Member, title:str, msg:str):
        ctx.response.defer(ephemeral=True)
        try:
            await member.send(embed=cr.emb(cr.yellow, title, msg))
            await ctx.send(embed=cr.emb(cr.yellow, title, msg),ephemeral=True)
        except:
            await ctx.send(embed=cr.emb(cr.red,"Dm not sent"),ephemeral=True)
            

    @commands.slash_command(name="warn",description="Warns the user")
    @commands.default_member_permissions(moderate_members=True)
    async def warn(self, ctx, member: disnake.Member, msg:str):
        await ctx.send(embed=cr.emb(cr.red, f"WARNING {member}",
                                  f'{member.mention} --> {msg}'),delete_after=10)
        try:
            await member.send(embed=cr.emb(cr.red, f"WARNING", msg))
        except:
            ...
