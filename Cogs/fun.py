import random
import json
import aiohttp
import requests
from bs4 import BeautifulSoup
import disnake
from disnake.ext import commands
from bot import cr
# from dotenv import load_dotenv
import os
# load_dotenv()


def extract_video_link(soup):
    link = soup.find('script', type='application/ld+json')
    link = json.loads(link.string) # if any problem switch to link.text
    link = link["contentUrl"]
    return link
proxies = { 
              "https" : "20.230.175.193:8080"
            }
def get(url):
    page = requests.get(url,proxies=proxies)
    htmlcontent = page.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    return soup


def setup(client: commands.Bot):
    client.add_cog(fun(client))


class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(name='nsfw')
    async def nsfw(self,ctx,term="porn",amount=1):
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

    
    @commands.command(name='xxx')
    async def xxx(self,ctx,*,term):
        if ctx.channel.is_nsfw():
            try:
                term = term.replace(" ","+")
                term_url = "https://www.xnxx.com/search/"+str(term)
                search_term = get(term_url)
                div = search_term.find('div', class_='mozaique cust-nb-cols')
                div = div.find_all('a')
                i = list(div) 
                i = random.choice(i)
                link = i.get('href')
                page = get("https://www.xnxx.com"+link)
                link = extract_video_link(page)
                await ctx.send(embed=cr.emb(cr.black,page.title.string))
                await ctx.send(link)
            except Exception:
                await ctx.send(embed=cr.emb(cr.red,"Try Again Later!"))

        else:
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))
