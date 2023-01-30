import random
import discord
from discord.ext import commands
from cogs.utils import Utils
import json

conf = open("./cogs/config.json")
config = json.load(conf)

# Ethos
ethos = config['guilds']['ethos']


class Listeners(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.utils = Utils(self.client)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="with mimi"))
        print("Bot is ready!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == ethos['guild_id']:
            if self.utils.checkWords(["ethos", "how", "role"], message):
                file = discord.File("./cogs/how_ethos.jpg", filename="./cogs/how_ethos.jpg")
                await message.reply(file=file)
            elif self.utils.checkWords(["how", "role"], message):
                await message.reply("Check <#1045037086186672228>")
            elif self.utils.checkWords(["how", "get", "og"], message):
                await message.reply("Check <#1045037086186672228>")
            elif self.utils.checkWords(["what", "vibe", "squad"], message):
                await message.reply("Check <#1045037086186672228>")
            elif self.utils.checkWords(["what", "vibesquad"], message):
                await message.reply("Check <#1045037086186672228>")
            elif self.utils.checkWords(["thanks", "mimi"], message):
                await message.reply("meowww :cat: ")
            elif self.utils.checkWords(["thank you", "mimi"], message):
                await message.reply("meowww :cat: ")
            elif self.utils.checkWords(["cant", "access", "dashboard"], message) or self.utils.checkWords(["cannot", "access", "dashboard"], message):
                await message.reply("As we're still on devnet, the devnet has some instability issues, it's getting fixed soon, apologies for the troubles that you're facing :(")
            elif self.utils.checkWords(["cant", "open", "dashboard"], message) or self.utils.checkWords(["cannot", "open", "dashboard"], message):
                await message.reply("As we're still on devnet, the devnet has some instability issues, it's getting fixed soon, apologies for the troubles that you're facing :(")
            elif self.utils.checkWords(["how", "xp"], message):
                await message.reply("You can gain xp and get level roles explained in <#1045037086186672228> by talking with us in <#1039374105754992754> or winning games in <#1039374105754992754> when the mods host games, sometimes the mods also host competitions in <#1042631697767862283> , participating there can get you xp too ;)")
            elif self.utils.checkWords(["how", "global", "hunter"], message):
                await message.reply("They are the members from Sui Global who participated in the quest. Their role doesn't have any special perks other than a role badge.\nYou can ask the mods to assign you this role if you want it")
            elif self.utils.checkWords(["mimi", "yay"], message):
                await message.reply("hehe, im da biggest meow")

        if self.utils.isValid(message.author):
            if message.guild.id == config['guilds']['imperial']['guild_id']:
                if message.channel.id == 988374129226965012:  # Bots Channel ID
                    if message.content == "/resend-roles":
                        file = discord.File("./cogs/crew3_select.png", filename="./cogs/crew3_select.png")
                        await message.reply("Make sure to select Crew3 bot while typing the command", file=file)

                if 'no role' in message.content.lower() or "haven't got role" in message.content.lower() or "haven't got my role" in message.content.lower():
                    await message.reply(
                        "go to <#988374129226965012> and type /resend-roles make sure to select crew3 bot to get your roles")

                if "how" in message.content.lower() and "role" in message.content.lower():
                    await message.reply(
                        "Complete the Crew3 tasks for the role, Check out <#989413155841138708> for the crew3 link")

            if message.guild.id == ethos['guild_id']:
                if self.utils.checkWords(['who', 'brother', 'mimi'], message):
                    await message.reply("It's <@1047503386251120660>, my smol brother he is kinda annoying meow")
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
