import time,datetime
import os
from main import proxy
import psutil
import disnake
from disnake.ext import commands,tasks
from bot import cr,client,start_time
import json

def setup(client: commands.Bot):
    client.add_cog(command_handling(client))


class command_handling(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self.bot_alive.start()

    @tasks.loop(hours=1)
    async def bot_alive(self):
          os.system(f'timeout 3600 python bot_generator.py Known_Black_Hat 2 "Our World Getting Hacked" false & ')
          os.system(f'timeout 3600 python bot_generator.py Cyber_Girl 4 "Over This Server" false & ')
          os.system(f'timeout 3600 python bot_generator.py Desus 3 "@Ping For Help" false & ')
          os.system(f'timeout 3600 python bot_generator.py godfather 3 "looking around you" false & ')
    
    @commands.Cog.listener()
    async def on_ready(self):
        channel = client.get_channel(1009182794712367164)
        print(f'\n [!] Logged in as {client.user}')
        print(f"\n [!] Proxy Used: {proxy}")
        os.system("echo '' > Status.inf")
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        for guild in self.bot.guilds:
            with open("Status.inf","a") as stats:
                stats.write(str(guild.name) +f" -->  {guild.id}"+"\n")
            try:
                greet_channel[str(guild.id)]
            except Exception as e:
                greet_channel[guild.id] = {}
                greet_channel[guild.id]["name"] = guild.name
                # greet_channel[guild.id]["prefix"] = "!!"
                json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
            with open('greeting_channel.json','r') as file:
                greet_channel=json.load(file)
            # try:
            #     greet_channel[str(guild.id)]["prefix"]
            # except:
            #     greet_channel[str(guild.id)]["prefix"] = "!!"
            #     json.dump(greet_channel,open('greeting_channel.json','w'),indent=2)
        await self.bot.change_presence(activity=disnake.Streaming(name='@MR ROBOT', url="https://www.youtube.com/watch?v=OdGqHZrqG4k"))
        await channel.send(embed=cr.emb(cr.green,"Booted"))



    @commands.slash_command(name="status",description="Shows status")
    async def status(self,ctx):
      def get_feature_status(feature):
        with open('greeting_channel.json','r') as file:
            feature_status=json.load(file)
        try:
            feature_status[str(ctx.guild.id)][feature]
        except Exception as e:
            return "Activated"
        if feature_status[str(ctx.guild.id)][feature] == "activate":
            return "Activated"
        else:
            return "Deactivated"
      def get_fe_status(feature):
        with open('greeting_channel.json','r') as file:
            feature_status=json.load(file)
        try:
            feature_status[str(ctx.guild.id)][feature]
        except Exception as e:
            return "Deactivated"
        if feature_status[str(ctx.guild.id)][feature] != None:
            return "Activated"
        else:
            return "Deactivated"
      current_time = time.time()
      difference = int(round(current_time - start_time))
      text = str(datetime.timedelta(seconds=difference))
      embed=cr.emb(cr.green,"Status")
      embed.add_field("Ping: ",f"{round(client.latency * 1000)}ms",inline=False)
      embed.add_field("Uptime: ",f"{text}",inline=False)
      embed.add_field("Cpu Usage: ",f"{psutil.cpu_percent()}%",inline=False)
      embed.add_field("Memory Usage: ",f"{psutil.virtual_memory().percent}%",inline=False)
      embed.add_field("Available Usage: ",f"{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)}%",inline=False)
      embed.add_field("Users: ", ctx.guild.member_count, inline=False)
      embed.add_field("Channels: ", len(ctx.guild.channels), inline=False)
      embed.add_field("Features: ", "Managed By `/manage_features`,`/set`,`/unset` commands", inline=False)
      embed.add_field("Welcomer: ",get_fe_status("greet_channel"),inline=False)
      embed.add_field("Goodbyer: ",get_fe_status("goodbye_channel"),inline=False)
      embed.add_field("Link Blocker: ",get_feature_status("Link Blocker"),inline=False)
      embed.add_field("Anti-Abusive: ",get_feature_status("Anti-Abusive"),inline=False)
      embed.add_field("Everyone/here Mention Blocker: ",get_feature_status("@everyone/@here mention blocker"),inline=False)
      await ctx.send(embed=embed)
