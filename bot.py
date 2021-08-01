import os
import random
from dotenv import load_dotenv
import time
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='~~')

registerList = []

@bot.event
async def on_ready():
    with open("regUsers.txt","r") as f:
        content = f.readlines()
    for entry in content:
        registerList.append(entry.split("--"))
    print(registerList)
    print(f'{bot.user.name} has connected to Discord!')
    



@bot.command(name='test', help='tests to see if the bot is connected to the server')
async def test(ctx):
    response = 'Bot is connected'
    await ctx.send(response)

@bot.command(name='register', help='registers new user for survey autofill')
async def register(ctx, name: str, server: str, discord: str):
    newUser = [name,server,discord]
    registerList.append(newUser)
    file1 = open("regUsers.txt","w")
    file1.write(newUser[0] + "--" + newUser[1] + "--" + newUser[2])
    file1.close()
    await ctx.send("Successfully enrolled")

@bot.command(name="reglist", help='shows registered users')
async def reglist(ctx):
    await ctx.send("Registered Users:")
    for user in registerList:
        await ctx.send(user[0] + ", " + user[1] + ", " + user[2])

@bot.command(name="ping", help="pings bot to verify connection")
async def ping(ctx):
    pingtime = time.time()
    pingms = await ctx.send("Pinging...")
    ping = time.time() - pingtime
    await ctx.send(":ping_pong:  time is `%.01f seconds`" % ping)

@bot.command(name="botlink", help="get link to invite CheezitBot to your server")
async def botlink(ctx):
    await ctx.send("Check your Dm's :wink:")
    await ctx.author.send("https://discord.com/api/oauth2/authorize?client_id=803438618999128064&permissions=8&scope=bot")

bot.run(TOKEN)