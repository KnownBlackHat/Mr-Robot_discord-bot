import disnake
from disnake.ext import commands
from main import *


def setup(client: commands.Bot):
    client.add_cog(command_error_handling(client))


class command_error_handling(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if 'You are missing at least one of the required roles: ' in str(
                error):
            await ctx.send(
                embed=cr.emb(cr.red, 'Sorry Permissions are missing! '))
        elif 'is not found' in str(error) and 'command' in str(error):
            with open('Logs/error.log', 'a') as file:
                file.write(f'Not Found: {error}\n')
            await ctx.send(embed=cr.emb(cr.red,'No Such Command is available! Use  `!!command`  for command list!'))
        elif 'required argument that is missing.' in str(error):
            await ctx.send(embed=cr.emb(cr.red, 'Arguments Are Missing!'))
        elif '404 HTTP response' in str(error) or '403 HTTP response' in str(
                error):
            await ctx.send(embed=cr.emb(cr.red, '🔎Search Stopped! 404 NOT FOUND')
                            )
        elif "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'url'" in str(
                error):
            await ctx.send(
                embed=cr.emb(cr.red, 'Api Overloaded RESTARTING API...'))
        elif 'This command cannot be used in private messages.' in str(error):
            await ctx.send(
                embed=cr.emb(cr.red, 'Command not available in private'))
        elif "Command raised an exception: AttributeError: 'DMChannel' object has no attribute 'is_nsfw'" in str(error):
          await ctx.send(
                embed=cr.emb(cr.red, 'Command not available in private'))
        elif "Command raised an exception: AttributeError: 'NoneType' object has no attribute 'play'" in str(error):
          ...
        else:
            with open('Logs/error.log', 'a') as file:
                file.write(f'Error: {error}\n')
                await ctx.send(
                    embed=cr.emb(cr.red, 'Oops! Something went wrong!',f'Error: {error}'))
