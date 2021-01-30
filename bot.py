import discord
import random
from discord.ext import commands


bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("working")

@bot.command()
async def h(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Use '!' to start a command\nAvailable commands:\n!cluck (eg !cluck hello nibba)\n!clear (eg !clear 10)")

@bot.command()
async def cluck(ctx, *, userString):
    await ctx.channel.purge(limit=1)
    ret = ""
    i = True
    for char in userString:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    await ctx.send(ret)
    
@bot.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)
    
@bot.command()
async def spamMove(ctx, member: discord.Member, number=2):
    await ctx.channel.purge(limit=1)
    channelList = []                            #gets list of all channels
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            channelList.append(channel)

    i = 0                                       #move user to random channel n times
    while i < number: 
        await member.edit(voice_channel=random.choice(channelList))
        i += 1
   
bot.run('ODA1MDk2NDE5OTA3NzMxNDk4.YBV6eA.noes8vB_P69RlJsRBS3f-pNttZw')