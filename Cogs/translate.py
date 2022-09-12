from disnake.ext import commands
from bot import cr
import os
os.system("pip install googletrans==3.1.0a0")
from googletrans import Translator


def setup(client: commands.Bot):
    client.add_cog(translate(client))


class translate(commands.Cog):
    def __init__(self, client):
        self.bot = client
    @commands.command(name="translate",aliases=['tr'])
    async def translate(self,ctx, lang, *, thing):
        translator = Translator()
        try:
            translation = translator.translate(thing, dest=lang)
        except Exception as e:
            if "invalid destination language" in str(e):
                await ctx.send(embed = cr.emb(cr.orange,f"Destination Translation Language List (DTLL) :",googletrans.LANGUAGES))
        await ctx.send(embed = cr.emb(cr.orange,f"Translation To {lang}",translation.text))
      
