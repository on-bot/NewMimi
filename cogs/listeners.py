import discord
from discord.ext import commands
import datetime
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
        if message.guild.id == ethos['guild_id']:
            knight = discord.utils.get(message.guild.roles, id=ethos['role_ids']['knight_id'])
            if message.author.top_role < knight:
                valid = False
            else:
                valid = True
        else:
            valid = True

        if valid:
            if message.content.startswith('.test'):
                await message.reply("Test Successfull")

        await self.client.process_commands(message)


async def setup(client):
    await client.add_cog(Listeners(client))
