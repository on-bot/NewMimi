import random
import discord
from discord.ext import commands
import json

conf = open("./cogs/config.json")
config = json.load(conf)

# Ethos
ethos = config['guilds']['ethos']


class Listeners(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="with mimi"))
        print("Bot is ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == ethos['guild_id']:
            knight = discord.utils.get(message.guild.roles, id=ethos['role_ids']['knight_id'])
            if message.author.top_role < knight:
                valid = False
            else:
                valid = True
        else:
            valid = True

        if valid:
            if message.guild.id == ethos['guild_id']:
                if message.content.lower() == "meow" or message.content.lower()[0:9] == "mimi meow":
                    await message.reply("nyaaa :cat: ")
                elif message.content.lower()[0:9] == "mimi come":
                    await message.reply("NO")
                elif message.content.lower() == "i love u" or message.content.lower()[0:13] == "mimi i love u":
                    await message.reply("I love u too :kissing_smiling_eyes: ")
                elif message.content.lower() == "mimi ttyl" or message.content.lower() == "mimi talk to you later":
                    await message.reply("noooooooo")
                elif message.content[-1] == "?" and "mimi" in message.content.lower():
                    await message.reply(random.choice(["yes", "no", "hmmmm", "meowww", "maybe", "idk", "perhaps"]))


async def setup(client):
    await client.add_cog(Listeners(client))
