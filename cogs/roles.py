import discord
from discord.ext import commands
import datetime
import json

conf = open("config.json")
config = json.load(conf)




# knight = discord.utils.get(guild.roles, id=knight_id)
# bishop = discord.utils.get(guild.roles, id=bishop_id)
# rook = discord.utils.get(guild.roles, id=rook_id)
# queen = discord.utils.get(guild.roles, id=queen_id)
# king = discord.utils.get(guild.roles, id=king_id)
# server_booster = discord.utils.get(guild.roles, id=server_booster_id)
# role_list = [knight, bishop, rook, queen, king, server_booster]


class Nouse(commands.Cog):

    def __init__(self, client):
        self.client = client




async def setup(client):
    await client.add_cog(Nouse(client))
