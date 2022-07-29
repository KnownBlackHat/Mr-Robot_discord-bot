import asyncio
from main import *
import disnake
import youtube_dl  # type: ignore
from disnake.ext import commands

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ""

ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": False,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address":
    "0.0.0.0",  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


def setup(client: commands.Bot):
    client.add_cog(Music(client))


class YTDLSource(disnake.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream))
        assert data

        if "entries" in data:
            # take first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        assert filename

        return cls(disnake.FFmpegPCMAudio(filename, **ffmpeg_options),
                   data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='music_command')
    async def music_help(self, ctx):
        await ctx.send(embed=cr.cr.emb(
            cr.blue, "Music Commands", """

`play [Multiple URLs | Search topic]`:
I'll play music from youtube

`volume [volume no.]`:
I'll change volume within 1% to 100%

`stop`:
I'll get disconnected from voice channel
                    
                               """))

    @commands.command(name='join')
    async def join(self, ctx, *, channel: disnake.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command(name='play')
    async def play(self, ctx, *, url):
        async with ctx.typing():
          ...
        await self.ensure_voice(ctx)
        player = await YTDLSource.from_url(url,loop=self.bot.loop,stream=True)
            
        ctx.voice_client.play(player,after=lambda e:  ctx.send(embed=cr.emb(cr.red,"Player Error", e))if e else None)
        
        await ctx.send(embed=cr.emb(cr.blue,"Playing...",f"""
Name: {player.title}
                                 
"""))

    @commands.command(name='volume')
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send(embed=cr.emb(cr.red,"Not connected to a voice channel."))

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(embed=cr.emb(cr.blue,"Volume",f"Changed volume to {volume}%"))

    @commands.command(name='stop')
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send(embed=cr.emb(
                    cr.red, "Your aren't connected to voice Channel",
                    "Connect to voice channel"))
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
