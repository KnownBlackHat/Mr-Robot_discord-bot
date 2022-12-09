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
    async def nsfw(self,ctx,search,amount:int=1):
        term=search
        if amount > 100:
            raise Exception("Amount Should be <= 100")
        await ctx.response.defer()
        if ctx.channel.is_nsfw():
            Header =  {'User-Agent' : "Magic Browser"}
            type=['best','top','new','rising','hot']
            choice = random.choice(type)
            # await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Searching {term} in {choice} category..."))
            # async with ctx.typing():    
            URL = f"https://www.reddit.com/r/{term}/{choice}.json?limit=1000" #{int(amount)}"
            async with aiohttp.request("GET",URL,headers=Header) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    nsfw_list=[]
                    try:
                        for d in data["data"]["children"]:
                            try: 
                                # await ctx.send(d["data"]["url_overridden_by_dest"])
                                nsfw_list.append(str(d["data"]["url_overridden_by_dest"]))
                            except KeyError:
                                if d["data"]["thumbnail"].startswith('http'):
                                    # await ctx.send(d["data"]["thumbnail"])
                                    nsfw_list.append(str(d["data"]["thumbnail"]))
                        # await ctx.send(embed=cr.emb(cr.black,"NSFW Command",f"🔎Search Of {term} in {choice} category Completed!"))
                        for i in range(amount):
                            await ctx.send(random.choice(nsfw_list))
                    except:
                        await ctx.send(embed=cr.emb(cr.red,"NSFW Command","Try Again Later"))
                else:
                    await ctx.send(embed=cr.emb(cr.red,"NSFW Command",f"{term} not found!"))
        else:
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"))

    # @commands.is_nsfw()
    @commands.slash_command(name='meme',description="Show you memes")
    async def meme(self, ctx):
       Header =  {'User-Agent' : "Magic Browser"}
       URL = "https://meme-api.herokuapp.com/gimme"
       async with aiohttp.request("GET",URL,headers=Header) as resp:
           if resp.status == 200:
              data = await resp.json()
              meme_pic = data["preview"][-2]
              await ctx.send(meme_pic)
           else:
              await ctx.send(embed=cr.emb(cr.red,"Meme Command",f"Meme API not responding!"),ephemeral=True)

    @commands.slash_command(name='nsfw_premium',description="Returns results from nsfw website")
    @commands.is_nsfw()
    async def xxx(self,ctx,search,amount=1):
        term = search
        if amount > 100:
            raise Exception("Amount Should be <= 100")
        await ctx.response.defer(ephemeral=True)
        if ctx.channel.is_nsfw():
          ufrm_term = term
          term = term.replace(" ","+")
          term_url = "https://www.xnxx.com/search/"+str(term)
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
                      await ctx.send(embed=cr.emb(cr.black,"Search Term: "+ufrm_term,"Video Title: "+page.title.string),ephemeral=True)
                      await ctx.send(link,ephemeral=True)
                      p = p+1
                  break
                except Exception as aw:
                  #print(aw)
                  continue
                # print(link)
              # break
          except Exception as ex:
              # print("Trying Again")
              await ctx.send(embed=cr.emb(cr.red,"Try Again Later!",ex),ephemeral=True)
                # continue

        else:
            await ctx.send(embed=cr.emb(cr.black,"NSFW Command", "Sorry Buddy! This is not nsfw channel!"),ephemeral=True)
