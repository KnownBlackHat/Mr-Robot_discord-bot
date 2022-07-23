import aiohttp
import disnake
from disnake.ext import commands
from main import *

def setup(client: commands.Bot):
    client.add_cog(fun(client))


reddit = praw.Reddit(client_id='gn-1O5327M3caeYY25qBIg',
                     client_secret='fNu5KPbonvUa6H-KqGD1nouGpYMfUA',
                     user_agent='MR ROBOT meme',
                     timeout=60)

headers={
         "Content-Type": "application/json",
  "Authorization": "Required for certain image types, Key for testing: `015445535454455354D6`"
        }
class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client


    @commands.command(name='nsfw')
    async def nsfw(self, ctx, topic='porn', amount=int(1)):
        if not str(ctx.message.author) == "Known_cr.black_hat#9645":
            amount = 1
        if ctx.channel.is_nsfw():
            async with ctx.typing():
                await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Searching {topic}..."))
            j = 0

            while j != amount:
                submission = reddit.subreddit(str(topic)).random()
                async with ctx.typing():
                    pass
                await ctx.send(submission.url)
                j = int(j + 1)
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Search Of {topic} Completed!"))
        else:
            await ctx.send(
                embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))


    @commands.command(name='meme')
    async def meme(self, ctx, amount=int(1)):
        if not str(ctx.message.author) == "Known_cr.black_hat#9645":
            amount = 1
        j = 0
        while j != amount:
            submission = reddit.subreddit('dankmemes').random()
            async with ctx.typing():
                pass
            await ctx.send(submission.url)
            j = int(j + 1)
'''
    @commands.command(name='nsfw')
    async def nsfw(self,ctx,search='boobs'):
      if ctx.channel.is_nsfw():
        async with aiohttp.ClientSession(headers=headers) as session:
          async with session.get(f"https://nekobot.xyz/api/image?type={search}") as response:
            if response.status == 200:
              json_data = await response.json()
              await ctx.send(json_data["message"])
            else:
              await ctx.send(embed=cr.emb(name="Error",value=f"The request was invalid.\nStatus code: {response.status}"))
      else:
        await ctx.send(
                embed=cr.emb(red, "Sorry Buddy! This is not nsfw channel!"))
'''
