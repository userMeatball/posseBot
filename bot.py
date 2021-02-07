import discord
import random
import time
from translate import Translator
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
                    !roll <value> (eg !roll 100) rolls a random number in range of value\n
                    !gamble <user> <text>(eg !gamble Meatball cook 100 gold) will roll random and pick a winner\n
                    !cointoss will flip a coin\n
                    !reverse <text> (eg !reverse hello) will reverse your text\n
                    !eightball <text> (eg !eightball will i win) tell your fortune on yes/no questions\n
                    !translate <language> <text> (eg !translate french you french pig!) translates your text\n
                    !rps <choice> (eg !rps rock) play rock, paper, scissors with the bot
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


@bot.command()                                      #!dm
@commands.has_role("botMaster")
async def dm(ctx, member: discord.Member, amount=1, sleep=0, *, userString):
    await ctx.channel.purge(limit=1)
    i = 0
    while i < amount:
        await member.send(f"**{userString}**")
        time.sleep(sleep)
        i += 1
        
        
@bot.command()                                      #!roll
async def roll(ctx, value):
    await ctx.channel.purge(limit=1)
    roll = random.randint(0, value)
    await ctx.send("You rolled " + str(roll))


@bot.command()                                      #!gamble
async def gamble(ctx, members: commands.Greedy[discord.Member], *, userString):
    players = [["", 0] for u in range(len(members))]
    i = 0
    for m in members:
        roll = random.randint(0, 100)
        await ctx.send(f"{m} rolled: " + str(roll))
        players[i] = [f"{m}", roll]
        i += 1
    
    winner = players[0][0]
    i = 0
    for w,p in players:
        if p > players[i][1]:
            winner = w
        elif p == players[i][1] and w != players[i][1]:
            winner += " drew with " + w
    i += 1
    
    await ctx.send("The winner is " + winner + "!")
    
    
@bot.command()                                      #!cointoss
async def cointoss(ctx):
    coin = ["heads", "tails"]
    await ctx.send(random.choice(coin))
    
    
@bot.command()                                      #!reverse
async def reverse(ctx, *, userString):
    await ctx.channel.purge(limit=1)
    string = str(userString) [::-1]
    await ctx.send(string)
    
    
@bot.command()                                      #!eightball
async def eightball(ctx):
    responses = ["It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"]
    
    await ctx.send(random.choice(responses))
    
@bot.command()                                      #!translate
async def translate(ctx, lang, *, userString):
    translator = Translator(to_lang=f"{lang}")
    translation = translator.translate(f"{userString}")
    await ctx.send(translation)

@bot.command()                                      #!rps
async def rps(ctx, userChoice):
    options = ["rock",
            "paper",
            "scissors"]

    cpuChoice = random.choice(options)

    await ctx.send("Rock...")
    time.sleep(1)
    await ctx.send("Paper...")
    time.sleep(1)
    await ctx.send("Scissors...")
    time.sleep(1)

    if userChoice == "rock"  and cpuChoice == "rock":
        await ctx.send("cpu chose rock too! it's a draw!")
    elif userChoice == "rock" and cpuChoice == "paper":
        await ctx.send("cpu chose paper! you lose!")
    elif userChoice == "rock" and cpuChoice == "scissors":
        await ctx.send("cpu chose scissors! you win!")
    elif userChoice == "paper" and cpuChoice == "paper":
        await ctx.send("cpu choose paper too! it's a draw!")
    elif userChoice == "paper" and cpuChoice == "rock":
        await ctx.send("cpu chose rock! you lose!")
    elif userChoice == "paper" and cpuChoice == "scissors":
        await ctx.send("cpu chose scissors! you win!")
    elif userChoice == "scissors" and cpuChoice == "scissors":
        await ctx.send("cpu choose scissors too! it's a draw!")
    elif userChoice == "scissors" and cpuChoice == "rock":
        await ctx.send("cpu chose scissors! you lose!")
    elif userChoice == "scissors" and cpuChoice == "paper":
        await ctx.send("cpu chose paper! you win!")
    else:
        await ctx.send("you didn't pick a valid choice")



