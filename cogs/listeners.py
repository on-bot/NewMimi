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
            if message.guild.id == config['guilds']['imperial']['guild_id']:
                if message.channel.id == 988374129226965012:   # Bots Channel ID
                    if message.content == "/resend-roles":
                        file = discord.File("./cogs/crew3_select.png", filename="./cogs/crew3_select.png")
                        await message.reply("Make sure to select Crew3 bot while typing the command", file=file)

                if 'no role' in message.content.lower() or "haven't got role" in message.content.lower() or "haven't got my role" in message.content.lower():
                    await message.reply(
                        "go to <#988374129226965012> and type /resend-roles make sure to select crew3 bot to get your roles")

                if "how" in message.content.lower() and "role" in message.content.lower():
                    await message.reply("Complete the Crew3 tasks for the role, Check out <#989413155841138708> for the crew3 link")
                    
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
