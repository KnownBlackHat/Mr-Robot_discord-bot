# TODO: Add features on/off toggle integration
# TODO: Add custom block list , protocol list

import disnake
from disnake.ext import commands
import re
from bot import cr,client
import json


def setup(client: commands.Bot):
    client.add_cog(anti_abusive(client))


class anti_abusive(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('greeting_channel.json','r') as file:
            prefixes=json.load(file)
        #print(message)
        #print(client.user.mention))
        #if client.user.mention:
        #    await message.channel.send(embed=cr.emb(cr.red,"Server Prefix",prefixes[str(message.guild.id)]["prefix"]))
        try:
            with open(f'Logs/{message.guild.name}.log', 'a') as msg:
                msg.write(
                    f'{message.channel.name}--> {message.author}: {message.content}\n'
                )
        except:
            pass



        msg_content = message.content.lower()




        curseWord = [
            'slut', 'f*ck' ,'fuck', 'pussy', 'bitch', 'ass', 'milf', 'loudfatty',
            'buttshaker', 'boob', 'penis', 'vagina', 'shit', 'dick', 'porn',
            'squirt', 'shemale', 'sperm', 'bsdm', 'sexylady',
            'swollen ovary', 'sexy', 'cunt', 'motherfliper'
                     ]
        block_word =  ['http://', 'https://', '://', '@here', '@everyone']



        if str(message.content) == f"<@{client.user.id}>":
            await message.channel.send(embed=cr.emb(cr.red,"Server Prefix",f'`{prefixes[str(message.guild.id)]["prefix"]}`')) 
        try:
          if  message.author.id == self.bot.user.id:
             ...
          elif not "name='Protocol_access'" in str(message.author.roles) :


            if any(word in msg_content for word in block_word):
              await message.delete()

            if not message.channel.is_nsfw():
               terms = [re.search(rf'\b{i}', msg_content) for i in curseWord]
               for j in terms:
                   if j != None:
                       await message.delete()
                       break
#              if any(word in msg_content for word in curseWord):
#                await message.delete()
                
        except Exception as e:
            print(e)
            
