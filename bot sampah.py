import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
sampah_organik = ["daun","kulit pisang","buah busuk"]
sampah_anorganik = ["botol plastik","kardus","plastik"]
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command()
async def pilih(ctx,sampah):
    if sampah in sampah_organik:
        await ctx.send("Masukkan dalam sampah organik")
    elif sampah in sampah_anorganik:
        await ctx.send('Masukkan dalam sampah anorganik')


bot.run("token botmu")






