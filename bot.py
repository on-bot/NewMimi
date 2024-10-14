import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Intents
intents = discord.Intents.all()
intents.members = True

commands_list = ['mimi ', 'Mimi ']

client = commands.Bot(intents=intents, command_prefix=commands_list, case_insensitive=True, help_command=None)


@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} loaded successfully.")


@client.command()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"{extension} unloaded successfully.")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description="Mimi here to help",
        colour=discord.Colour.purple()
    )
    embed.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar.url)
    embed.add_field(name="General", value="`credits`", inline=False)
    embed.add_field(name="Moderation", value="`--Secret--`", inline=False)
    embed.add_field(name="Fun", value="`say`, `cat`, `selfie`, `rps`, `catfact`, `kill`, `tickle`")
    await ctx.send(embed=embed)
  
async def mainload():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await mainload()
    await client.start(os.environ["DISCORD_TOKEN"])


asyncio.run(main())
