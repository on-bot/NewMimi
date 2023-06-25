from discord.ext import commands
import json
import asyncio
import discord
import os

conf = open("./cogs/config.json")
config = json.load(conf)

# Torts
torts = config['guilds']['torts']


class Torts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == torts["guild_id"]:
            tort_team = message.guild.get_role(torts["role_ids"]["tortteam"])
            communitytort = message.guild.get_role(torts["role_ids"]["communitytort"])
            user = message.author
            if not tort_team in user.roles and not communitytort in user.roles:
                links = [".com", ".net", ".org", ".co", ".us", ".ml", ".tk", ".ga", ".cf", ".gq", "https", ".io"
                         "MINTING LIVE NOW", "http", "👉 http", "mint.io", "claim here", ]
                white = ["tenor"]
                if any(word in message.content.lower() for word in links) and any(word not in message.content.lower() for word in white):
                    print("shoulda delete")
                    await message.delete()
    
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
