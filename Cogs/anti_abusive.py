import disnake
from disnake.ext import commands


def setup(client: commands.Bot):
    client.add_cog(anti_abusive(client))


class anti_abusive(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            with open(f'Logs/{message.guild.name}.log', 'a') as msg:
                msg.write(
                    f'{message.channel.name}--> {message.author}: {message.content}\n'
                )
        except:
            pass
        msg_content = message.content.lower()
        curseWord = [
            'slut', 'fuck', 'pussy', 'bitch', ' ass ', 'milf', 'loudfatty',
            'buttshaker', 'boob', 'penis', 'vagina', 'shit', 'dick', 'porn',
            'squirt', 'gay', 'shemale', 'lesbian', 'sperm', 'bsdm', 'sexylady',
            'swollen ovary', 'sexy', 'rajnish tatti', 'cunt', 'motherfliper'
        ]
        block_word =  ['http://', 'https://', '://', '@here', '@everyone']
        #    print(message.author.roles)
        # delete curse word if match with the list
        try:
          if  message.author.id == self.bot.user.id:
             ...
          elif not "name='Protocol_access'" in str(message.author.roles) :
          
            if any(word in msg_content for word in block_word):
              await message.delete()
            if not message.channel.is_nsfw():
              if any(word in msg_content for word in curseWord):
                await message.delete()
                
        except:
            ...
            