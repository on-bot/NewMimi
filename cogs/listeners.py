import discord
from discord.ext import commands
import datetime


class Listeners(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="with mimi"))
        print("Bot is ready!")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.guild.id == 995429222497652796 and message.channel.id == 996666624058867774:
            channel = self.client.get_channel(997483582312427580)
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                title=f"Deleted Message by {message.author.name + '#' + str(message.author.discriminator)}"
            )
            embed.add_field(name="Message:\n", value=message.content, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='\u200b')
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 1039314094081183824:  # ethos
            knight = discord.utils.get(message.guild.roles, id=1045279846953132072)
            bishop = discord.utils.get(message.guild.roles, id=1045280247903424582)
            rook = discord.utils.get(message.guild.roles, id=1045279621958090872)
            queen = discord.utils.get(message.guild.roles, id=1045274556379701259)
            king = discord.utils.get(message.guild.roles, id=1045274429141299250)
            server_booster = discord.utils.get(message.guild.roles, id=1040681728232136795)
            role_list = [knight, bishop, rook, queen, king, server_booster]

            if check_list(role_list, message.author.roles):
                valid = True
            else:
                valid = False

        else:
            valid = True
        if valid:
            if message.guild.id == 988374126681030656 and message.channel.id == 988374129226965012:
                if message.content == "/resend-roles":
                    file = discord.File("crew3_select.png", filename="crew3_select.png")
                    await message.reply("Make sure to select Crew3 bot while typing the command", file=file)

            if message.guild.id == 988374126681030656:
                if 'no role' in message.content or "haven't got role" in message.content or "haven't got my role" in message.content:
                    await message.reply(
                        "go to <#988374129226965012> and type /resend-roles make sure to select crew3 bot to get your roles")

            if message.guild.id == 1039314094081183824:
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

        await client.process_commands(message)


async def setup(client):
    await client.add_cog(Listeners(client))
