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

bot.run("MTA4NjU2MjgxMDE2ODg4OTQ1NA.GkXbuD.8FEF-yhH3O7I-2aZ7_xniJm269B0tlpU3amx8I")