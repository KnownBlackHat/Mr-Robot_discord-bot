from disnake.ext import commands
from bot import cr
import disnake
import os
# os.system("pip install googletrans==3.1.0a0")
from googletrans import Translator
import googletrans as gt

def setup(client: commands.Bot):
    client.add_cog(translate(client))

# language_list = ["h","b"]
# for i in gt.LANGUAGES:
#     language_list.append(gt.LANGUAGES[i])
# a=commands.option_enum([language_list])

# async def autocomp_langs(inter: disnake.ApplicationCommandInteraction, user_input: str):
#     return [lang for lang in language_list]

class translate(commands.Cog):
    def __init__(self, client):
        self.bot = client
    @commands.slash_command(name="translate",description="Returns translated text")
    async def translate(self,ctx, language, message):
        translator = Translator()
        try:
            translation = translator.translate(message, dest=language)
            await ctx.send(embed = cr.emb(cr.orange,f"Translation {translation.src} To {language}",translation.text))
        except Exception as e:
            if "invalid destination language" in str(e):
                await ctx.send(embed = cr.emb(cr.orange,f"Destination Translation Language List (DTLL) :",str(gt.LANGUAGES).replace(",","\n")))
      
