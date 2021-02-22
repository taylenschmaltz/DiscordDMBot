import discord
from discord.ext.commands import Bot, Greedy
from discord.ext import tasks, commands
from keep_alive import keep_alive
import asyncio
from discord import User
import io
import os
import platform
import colorsys
import random
import time

intents = discord.Intents.default()
intents.members = True
client = discord.Client()

client = Bot(command_prefix = '>', intents=intents)

@client.event
async def on_ready():
  print('Online')

@client.command()
@commands.has_permissions(manage_roles = True)
async def ids(ctx, role: discord.Role): 
    await ctx.send("\n".join([str(member.id) for member in role.members]))

@client.command()
@commands.has_permissions(manage_roles = True)
async def dm(ctx, users: Greedy[User], *, message):
    for user in users:
      await user.send(message)

@client.command()
async def dm_all(ctx, *, args=None):
  if args != None:
    members = ctx.guild.members
    for member in members:
      try:
        await member.send(args)
        await ctx.send("''" + args + "' sent to: " + member.name)
      except:
        await ctx.send("couldn't send")

@client.command()
async def commands(ctx):
  embed = discord.Embed(title = 'Commands | Prefix = >', description = '**ids:** This command is used to get a list of member ids from the users that belong to a specific role (Requires "Manage Roles" ability to run). \n \n Example: ```>ids @moderators``` (returns a list of member ids which you will then copy to use when running the >dm command. \n \n **dm:** This command is used to dm a single user or multiple users (Requires "Manage Roles" ability to run). \n Example: ```>dm @name @name @name (unlimited amount of users allowed) message.``` \n Also, you can use member ids as well: ```>dm @446964352541321246 @746964352311321246 @346962352541321246 message``` \n ', color = discord.Colour.blue())
  await ctx.send(embed=embed)


keep_alive()
client.run(os.getenv('TOKEN'))
