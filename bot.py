import discord
import random
from discord.ext import commands
from discord.ext.commands import has_role


bot = commands.Bot(command_prefix = '!')

@bot.event                                      #on_ready
async def on_ready():
    print("working")

@bot.command()                                      #help
async def h(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("""Use '!' to start a command\n
                    Available commands:\n
                    !cluck <text> (eg !cluck hello) transforms text into 'cluck' format\n
                    !clear <amount> (eg !clear 10) clears specified amount of messages in chat\n
                    !roll <range> <amount)> (eg !roll 100 1) rolls a random number between the range and the amount of times to roll\n
                    !dm <user> <amount> <text> (eg !dm cook 1 wagwan) bot will dm user amount of times specified
                    """)

@bot.command()                                      #!cluck
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
    
@bot.command()                                      #!clear
@commands.has_role("botMaster")
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=amount)
    
@bot.command()                                      #!spamMove
@commands.has_role("botMaster")
async def spamMove(ctx, member: discord.Member, number=2):
    await ctx.channel.purge(limit=1)
    channelList = []    #gets list of all channels
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            channelList.append(channel)

    i = 0
    while i < number: 
        await member.edit(voice_channel=random.choice(channelList))   #move user to random channel n times
        i += 1
        
@bot.command()                                      #!roll
async def roll(ctx, number=100, amount=1):
    await ctx.channel.purge(limit=1)
    i = 0
    while i < amount:
        await ctx.send(random.randint(0, number))
        i += 1
   
@bot.command()                                      #!dm
@commands.has_role("botMaster")
async def dm(ctx, member: discord.Member, amount=1, *, userString):
    await ctx.channel.purge(limit=1)
    i = 0
    while i < amount:
        await member.send(f"**{userString}**")
        i += 1

   
bot.run('ODA1MDk2NDE5OTA3NzMxNDk4.YBV6eA.FIGCYs9nmsnEH1V5ac-7zR09I3Y')