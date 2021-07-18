from discord.ext import commands
import discord
import asyncio

import config


intents = discord.Intents.all()
TOKEN = config.Token
prefix = "¥"

bot = commands.Bot(command_prefix=prefix,intents=intents)


bot.load_extension("Cogs.default")
bot.load_extension("Cogs.stage-musicbot")

bot.run(TOKEN)