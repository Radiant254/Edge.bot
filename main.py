import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "!", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author} como vai?')

@client.command()
async def dado(ctx, numero):
  variavel = random.randint(1,int(numero))
  await ctx.send(f'O número que saiu no dado é {variavel}')

client.run('token')