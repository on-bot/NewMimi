import asyncio
import os
import discord
from discord.ext import commands

# Intents
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(intents=intents, command_prefix='.', case_insensitive=True)


@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} loaded successfully.")


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} unloaded successfully.")


async def mainload():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await mainload()
    await client.start("TOKEN")


asyncio.run(main())
