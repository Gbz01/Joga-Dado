import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send (f'Seja bem vindo, {ctx.author}!')

@client.command()
async def dado(ctx, numero):
  num = random.randint(1, int(numero))
  await ctx.send (f'O número que saiu no dado é {num}. Jogado por {ctx.author}')

client.run('ODkyOTI0MzYzNDM3OTMyNTc0.YVT-nQ.5WRxfF_j_7HITHX471D6p5ryOXU')