import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
   print("ready")

@client.command()
async def dm_all(ctx, *, args=None):
   if args != None:
      members = ctx.guild.members
      for member in members:
         try:
            await member.send(args)
         except:
            print("No work")
   else:
      await ctx.send("Problème détecté")

client.run("Your Token")