import disnake
from disnake.ext import commands
from bot import cr
import os
os.system('pip install googletrans==3.1.0a0')
from googletrans import Translator

def setup(client: commands.Bot):
    client.add_cog(translate(client))


class translate(commands.Cog):
    def __init__(self, client):
        self.bot = client
    @commands.command(aliases=["tr","translate"])
    async def translate(self,ctx, lang, *, thing):
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        await ctx.send(embed = cr.emb(cr.orange,f"Translation To {lang}",translation.text))
      
