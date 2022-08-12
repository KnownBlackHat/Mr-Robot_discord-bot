import random
from secrets import choice
import aiohttp
import disnake
from disnake.ext import commands
from bot import cr
from dotenv import load_dotenv
import os
load_dotenv()

def setup(client: commands.Bot):
    client.add_cog(fun(client))

client_id = os.getenv('client_id')

client_secret = os.getenv('client_secret')
user = os.getenv('user')
passw = os.getenv('passw')
# reddit = apraw.Reddit(client_id = client_id,
#                      client_secret = client_secret,
#                      password=passw,
#                      user_agent='Mr Robot',
#                      username=user)

# headers={
#          "Content-Type": "application/json",
#   "Authorization": "Required for certain image types, Key for testing: `015445535454455354D6`"
#         }
class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(name='nsfw')
    async def nsfw(self,ctx,term,amount=1):
        if ctx.channel.is_nsfw():
            Header =  {'User-Agent' : "Magic Browser"}
            type=['best','top','new','rising','hot']
            choice = random.choice(type)
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Searching {term} in {choice} category..."))
            async with ctx.typing():    
                URL = f"https://www.reddit.com/r/{term}/{choice}.json?limit={int(amount)}"
                async with aiohttp.request("GET",URL,headers=Header) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        try:
                            for d in data["data"]["children"]:
                                try: 
                                    await ctx.send(d["data"]["url_overridden_by_dest"])
                                except KeyError:
                                    if d["data"]["thumbnail"].startswith('http'):
                                        await ctx.send(d["data"]["thumbnail"])
                            await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Search Of {term} in {choice} category Completed!"))
                        except:
                            await ctx.send(embed=cr.emb(cr.red,"NSFW Command","Try Again Later"))
                    else:
                        await ctx.send(embed=cr.emb(cr.red,"NSFW Command",f"{term} not found!"))
        else:
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))

    # @commands.command(name='nsfw')
    # async def nsfw(self, ctx, topic='porn', amount=1):
    #     if not str(ctx.message.author) == "Known_black_hat#9645":
    #         amount = 1
    #     if ctx.channel.is_nsfw():
    #         async with ctx.typing():
    #             await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Searching {topic}..."))
    #         j = 0

    #         while j != amount:
    #             submission = reddit.subreddit(str(topic)).random()
    #             #submission = await reddit.subreddit(str(topic)).random()
    #             async with ctx.typing():
    #                 pass
    #             await ctx.send(submission.url)
    #             j = int(j + 1)
    #         await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Search Of {topic} Completed!"))
    #     else:
    #         await ctx.send(
    #             embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))

    
    @commands.command(name='meme')
    async def meme(self, ctx, amount=int(1)):
        Header =  {'User-Agent' : "Magic Browser"}
        type=['best','top','new','rising','hot']
        choice = random.choice(type)
        await ctx.send(embed=cr.emb(cr.black,"Meme Command",f"🔎Searching Meme in {choice} category..."))
        async with ctx.typing():    
            URL = f"https://www.reddit.com/r/meme/{choice}.json?limit={int(amount)}"
            async with aiohttp.request("GET",URL,headers=Header) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    try:
                        for d in data["data"]["children"]:
                            try: 
                                await ctx.send(d["data"]["url_overridden_by_dest"])
                            except KeyError:
                                if d["data"]["thumbnail"].startswith('http'):
                                    await ctx.send(d["data"]["thumbnail"])
                        await ctx.send(embed=cr.emb(cr.black,"Meme Command",f"🔎Search Of Meme in {choice} category Completed!"))
                    except:
                        await ctx.send(embed=cr.emb(cr.red,"Meme Command","Try Again Later"))
                else:
                    await ctx.send(embed=cr.emb(cr.red,"Meme Command",f"Meme not found!"))

    '''@commands.command(name='nsfw')
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
