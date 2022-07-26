import disnake
from disnake.ext import commands
from bot import cr
import json

def setup(client: commands.Bot):
    client.add_cog(moderation(client))


class moderation(commands.Cog):
    def __init__(self, client):
        self.bot = client

    
#clear

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, context, amount=1):
        await context.message.channel.purge(limit=int(amount) + 1)
        print("\n [!] Chat Clearing System Was Activated!")


    @commands.command(name='changeprefix')
    @commands.has_permissions(manage_guild=True)
    async def changeprefix(self, ctx, *,prefix):
        with open('greeting_channel.json','r') as file:
                prefixes=json.load(file)
        if prefix.startswith('"') and prefix.endswith('"'):
            prefix = prefix.replace('"','')
        elif prefix.startswith("'") and prefix.endswith("'"):
            prefix = prefix.replace("'","")
        prefixes[str(ctx.guild.id)]["prefix"] = prefix
        json.dump(prefixes,open('greeting_channel.json','w'),indent=2)
        await ctx.send(embed=cr.emb(cr.green,"New Server Prefix",f'`{prefix}`'))

    @commands.command(name='addrole', aliases=['ar'])
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: disnake.Member, *, roll: disnake.Role):
        await ctx.message.delete()
        role = disnake.utils.get(user.guild.roles, name=str(roll))
        await user.add_roles(role)
        await ctx.send(embed=cr.emb(cr.green, "Role Assigned",
                                  f"{user.mention} Has Got  `{role}`  Role !"))
        try:
            await user.send(
                embed=cr.emb(cr.green, "Role Assigned",
                          f" You got `{role}` Role In {ctx.guild.name} !"))
        except:
            ...

    @commands.command(name='rmrole', aliases=['rr'])
    @commands.has_permissions(manage_roles=True)
    async def rmrole(self, ctx, user: disnake.Member, *, roll: disnake.Role):
        await ctx.message.delete()
        role = disnake.utils.get(user.guild.roles, name=str(roll))
        await user.remove_roles(role)
        await ctx.send(
            embed=cr.emb(cr.red, "Role Removed",
                      f"{user.mention} Was Removed  `{role}` Role !"))
        try:
            await user.send(embed=cr.emb(
                cr.red, "Role Removed",
                f"You got removed from `{role}` Role In {ctx.guild.name}!"))
        except:
            ...

    @commands.command(name='unban', aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, context, *, member):
        banned_users = await context.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await context.guild.unban(user)
                await context.send(
                    embed=cr.emb(cr.green,"Unbanned",f'Unbanned: {user}'))
                try:
                    await member.send(embed=cr.emb(
                        name=
                        f'You Were Unbanned From The {context.guild.name} Server!'
                    ))
                except:
                    pass

                return

    @commands.command(name='ban', aliases=['b'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: disnake.Member, *, reason=None):
        try:
            await member.send(embed=cr.emb(cr.red,f'You Were Banned From The {context.guild.name} Server!',f'Reason: {reason}'))
        except:
            pass
        await member.ban(reason=reason)
        await context.send(
            embed=cr.emb(cr.red,"Banned",f'Banned: {member} Reason: {reason}'))

    @commands.command(name="mute", aliases=['m'])
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: disnake.Member, *, reason=None):
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
            cr.red,"Muted",f" Muted: {member.mention} Reason: {reason}"))
        await member.send(embed=cr.emb(
            cr.red,
            f'You are Muted in the {guild.name} server',f'Reason: {reason}'))

    @commands.command(name="unmute", aliases=['um'])
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: disnake.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await ctx.send(
            embed=cr.emb(cr.green,"Unmuted",f"Unmuted {member.mention}"))
        await member.send(embed=cr.emb(cr.green,
            f'You are Unmuted in the {guild.name} server!',' 😉😉Enjoy😉😉!'))

    @commands.command(name='kick', aliases=['bye','goodbye'])
    @commands.has_permissions(kick_members=True)
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

    @commands.command(name="warn")
    @commands.has_permissions(manage_guild=True)
    async def warn(self, ctx, member: disnake.Member, *, msg):
        await ctx.message.delete()
        await ctx.send(embed=cr.emb(cr.red, f"WARNING {member}",
                                  f'{member.mention} --> {msg}'))
        try:
            await member.send(embed=cr.emb(cr.red, f"WARNING", msg))
        except:
            ...
