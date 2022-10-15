import time,datetime
import os
import psutil
import disnake
from disnake.ext import commands
from bot import cr,client,start_time
import json

def setup(client: commands.Bot):
    client.add_cog(command_handling(client))


class command_handling(commands.Cog):
    def __init__(self, client):
        self.bot = client

    
    @commands.Cog.listener()
    async def on_ready(self):
        channel = client.get_channel(1009182794712367164)
        #os.system('clear')
        print(f'\n [!] Logged in as {client.user}')
#         print(f'\n[!] Bot name: {client.user} Id: {client.user.id} \n Bot Owner: {client.owner}')
        os.system('curl -s ifconfig.me >>ip.txt ; echo '' >> ip.txt')
        with open('greeting_channel.json','r') as file:
            greet_channel=json.load(file)
        for guild in self.bot.guilds:
            with open("Status.inf","a") as stats:
                stats.write(str(guild.name) +"\n")
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
        await self.bot.change_presence(status=disnake.Status.idle,
                                       activity=disnake.Game(name='@MR ROBOT'))
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
