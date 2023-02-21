from discord.ext import commands
import json
import discord
import re

conf = open("./cogs/config.json")
config = json.load(conf)

# Ethos
dev = config['guilds']['dev']


class DevInvites(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def check_roles(self, guild, user_id, invite):
        check_dict = {}
        user = guild.get_member(int(user_id))
        if user is None:
            return
        check_dict[5] = dev["role_ids"]["5"]
        check_dict[15] = dev["role_ids"]["15"]
        check_dict[30] = dev["role_ids"]["30"]
        check_dict[50] = dev["role_ids"]["50"]
        check_dict[100] = dev["role_ids"]["100"]
        check_dict[200] = dev["role_ids"]["200"]
        check_dict[400] = dev["role_ids"]["400"]
        if invite == 5:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 15:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 30:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 50:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 100:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 200:
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
        elif invite == 400:
            await user.add_roles(discord.utils.get(guild.roles, id=check_dict[400]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
            await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))

    async def give_role(self, name, disc, invites):
        totalInvites = invites
        guild = self.client.get_guild(dev['guild_id'])
        user = discord.utils.get(guild.members, name=name, discriminator=disc)
        if totalInvites >= 400:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["400"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 400)
        elif totalInvites >= 200:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["200"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 200)
        elif totalInvites >= 100:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["100"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 100)
        elif totalInvites >= 50:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["50"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 50)
        elif totalInvites >= 30:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["30"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 30)
        elif totalInvites >= 15:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["15"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 15)
        elif totalInvites >= 5:
            five_invites_role = discord.utils.get(guild.roles, id=dev["role_ids"]["5"])
            await user.add_roles(five_invites_role)
            await self.check_roles(guild, user.id, 5)

    @staticmethod
    def get_invites_num(invites_string):
        num_pattern = r"\*\*(\d+)\*\* invites\."
        num_match = re.search(num_pattern, invites_string)
        if num_match:
            return int(num_match.group(1))
        else:
            return 0

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == dev["channel_ids"]["mod_bots"]:
            if message.author.id == 720351927581278219:
                for embed in message.embeds:
                    invites = self.get_invites_num(embed.description)
                    title = embed.title
                    name, desc = title.strip('**').split('#')
                    await self.give_role(name, desc, invites)


async def setup(client):
    await client.add_cog(DevInvites(client))
