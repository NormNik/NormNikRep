import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'/We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'/Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def Wdiscord(ctx):
    await ctx.send("https://discord.com/")
@bot.command()
async def HELP(ctx):
    await ctx.send("hello - print welcom messenge\n he - hehehehehe\n Wdiscord - discord's page")

bot.run("")
