from discord.ext import commands
import discord
import json

conf = open("./cogs/config.json")
config = json.load(conf)

# Ethos
ethos = config['guilds']['ethos']


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    def has_higher_role(self, member, role_id):
        guild = member.guild
        role = discord.utils.get(guild.roles, id=role_id)
        if member.top_role.position >= role.position:
            return True
        else:
            return False

    def isValid(self, member):
        if member.guild.id == ethos['guild_id']:
            vibe_squad = discord.utils.get(member.guild.roles, id=ethos['role_ids']['vibe_squad_id'])
            knight = discord.utils.get(member.guild.roles, id=ethos['role_ids']['knight_id'])
            if member.top_role == vibe_squad:
                second_highest_role = [role for role in member.roles][-2]
                if second_highest_role.position >= knight.position:
                    return True
                else:
                    return False
            else:
                role = discord.utils.get(member.guild.roles, id=ethos['role_ids']['knight_id'])
                if member.top_role.position >= role.position:
                    return True
                else:
                    return False
        else:
            return True

    async def winner_embed(self, ctx, text):
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(name=text)
        await ctx.reply(embed=embed)

    async def loser_embed(self, ctx, text):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name=text)
        await ctx.reply(embed=embed)

    async def draw_embed(self, ctx, text):
        embed = discord.Embed(colour=discord.Colour.dark_gray())
        embed.set_author(name=text)
        await ctx.reply(embed=embed)

    async def blue_embed(self, msg, text):
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name=text)
        msg = await msg.reply(embed=embed)
        return msg


async def setup(client):
    await client.add_cog(Utils(client))
