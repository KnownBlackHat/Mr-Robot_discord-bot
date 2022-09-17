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


def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = f"http://{random.choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}"
    return proxy
  
async def get(url):
  while True:
    try:
      #proxy=proxy_generator()
      # print(f"Proxy currently being used: {proxy}")
      async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(url,ssl=False,timeout=7) as response:
              htmlcontent = await response.text()
              break
    except:
      # print("Connection error, looking for another proxy")
      continue
  soup = BeautifulSoup(htmlcontent, "html.parser")
  return soup


def setup(client: commands.Bot):
    client.add_cog(fun(client))


class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client
    @commands.is_nsfw()
    @commands.slash_command(name='nsfw',description="Shows You Nsfw Content")
    async def nsfw(self,ctx,term,amount=1):
        if ctx.channel.is_nsfw():
            Header =  {'User-Agent' : "Magic Browser"}
            type=['best','top','new','rising','hot']
            choice = random.choice(type)
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Searching {term} in {choice} category..."))
            # async with ctx.typing():    
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

    @commands.is_nsfw()
    @commands.slash_command(name='meme',description="Show you memes")
    async def meme(self, ctx, amount=1):
        Header =  {'User-Agent' : "Magic Browser"}
        type=['best','top','new','rising','hot']
        choice = random.choice(type)
        await ctx.send(embed=cr.emb(cr.black,"Meme Command",f"🔎Searching Meme in {choice} category..."))
        # async with ctx.typing():    
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

    #@commands.is_owner()
    @commands.is_nsfw()
    @commands.slash_command(name='xxx',description="Returns Results from xnxx.com")
    async def xxx(self,ctx,term,amount=1):
        if ctx.channel.is_nsfw():
          await ctx.send(embed=cr.emb(cr.yellow,"Results may take time, so hold on!"),delete_after=10)
          stri = ""
          for n in term:
            stri = stri+" "+n
          term = stri
          if term == "":
            term = "porn"
          ufrm_term = term
          term = term.replace(" ","+")
          term_url = "https://www.xnxx.com/search/"+str(term)
          # print(await get(term_url))
          # async with ctx.typing():
          try:
              p=0
              while True:
                try:
                  search_term = await get(term_url)
                  div = search_term.find('div', class_='mozaique cust-nb-cols')
                  div = div.find_all('a')
                  i = list(div)
                  while p != int(amount):
                      i = random.choice(i)
                      link = i.get('href')
                      page = await get("https://www.xnxx.com"+link)
                      link = extract_video_link(page)
                      await ctx.send(embed=cr.emb(cr.black,"Search Term: "+ufrm_term,"Video Title: "+page.title.string))
                      await ctx.send(link)
                      p = p+1
                  break
                except Exception as aw:
                  #print(aw)
                  continue
                # print(link)
              # break
          except Exception as ex:
              # print("Trying Again")
              await ctx.send(embed=cr.emb(cr.red,"Try Again Later!",ex))
                # continue

        else:
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))
