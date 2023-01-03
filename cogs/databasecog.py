import os

from discord.ext import commands
from pymongo import MongoClient


class Database(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.cluster = MongoClient(os.environ["MONGO_API"])
        self.db = self.cluster["discord"]
        self.collection = self.db["ethos_xp_cat"]

    def query(self):
        return self.collection


async def setup(client):
    await client.add_cog(Database(client))
