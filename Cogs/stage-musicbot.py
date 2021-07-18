import datetime

from discord.ext import commands
import discord
import ffmpeg
import asyncio


class StargeChannelMusicbot(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.guild_id = 603582455756095488
        #self.joinchannel_id = 865846144286064670
        self.joinchannel_id = 603582455756095492

    @commands.Cog.listener()
    async def on_ready(self):
        stage_channel = self.bot.get_channel(self.joinchannel_id)
        stagechannel = await stage_channel.connect()
        #await self.bot.get_guild(self.guild_id).me.edit(suppress = False)
        #await self.bot.get_guild(self.guild_id).me.request_to_speak()
        stagechannel.play(discord.FFmpegPCMAudio(source="firesound.mp3"))


def setup(bot):
    return bot.add_cog(StargeChannelMusicbot(bot))