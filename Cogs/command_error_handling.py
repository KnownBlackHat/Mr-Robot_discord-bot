import traceback
import os
import disnake
from disnake.ext import commands
from bot import cr


def setup(client: commands.Bot):
    client.add_cog(command_error_handling(client))


class command_error_handling(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):


        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send(
                embed=cr.emb(cr.red, 'Sorry Permissions are missing! '),ephemeral=True)


        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(embed=cr.emb(cr.red,'No Such Command is available! Use  `<server prefix>command`  for command list!'),ephemeral=True)


        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(embed=cr.emb(cr.red, 'Arguments Are Missing!'),ephemeral=True)


        elif '404 HTTP response' in str(error) or '403 HTTP response' in str(
                error):
            await ctx.send(embed=cr.emb(cr.red, '🔎Search Stopped! 404 NOT FOUND'),ephemeral=True)


        elif isinstance(error,AttributeError):
            await ctx.send(embed=cr.emb(cr.red, 'ERROR',str(error)),ephemeral=True)

        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=cr.emb(cr.red,'Argument Error','Pass valid argument'),ephemeral=True)

        elif 'This command cannot be used in private messages.' in str(error):
            await ctx.send(embed=cr.emb(cr.red, 'Command not available in private'),ephemeral=True)

        elif  isinstance(error, disnake.errors.Forbidden):
            await ctx.send(embed=cr.emb(cr.red,'Forbidden'),ephemeral=True)

        # elif "Command raised an exception: AttributeError: 'DMChannel' object has no attribute 'is_nsfw'" in str(error):
        #   await ctx.send(
        #         embed=cr.emb(cr.red, 'Command not available in private'))


        # elif "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'play'" in str(error):
        #   ...


        elif "Cannot send messages to this user" in str(error):
          ...



        # elif "Access denied | discord.com used Cloudflare to restrict access" in str(error):
        #   os.system("kill 1")


        else:
            with open('Logs/error.log', 'a') as file:
                file.write('\n\n')
                file.write('-'*10)
                file.write(f'Error: {str(error)}')
                await ctx.send(
                    embed=cr.emb(cr.red, 'Oops! Something went wrong!',f'Error: {str(error)}'),ephemeral=True)