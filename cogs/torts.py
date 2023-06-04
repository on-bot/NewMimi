from discord.ext import commands
import json
import asyncio

conf = open("./cogs/config.json")
config = json.load(conf)

# Torts
torts = config['guilds']['torts']


class Torts(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        print(torts["guild_id"])
        if channel.guild.id == torts["guild_id"]:
            await asyncio.sleep(2)
            print("test")
            first_message = [message async for message in channel.history(limit=1, oldest_first=True)][0]
            if first_message.author.id == 557628352828014614:
                print("should be no error")
                nameO = first_message.mentions[0].name
                await channel.edit(name=nameO)


async def setup(client):
    await client.add_cog(Torts(client))
