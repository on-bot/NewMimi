import os
import discord
import requests
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gib(self, ctx, role: discord.Role):
        """ Assigns Roles to Given list of Usernames (Works Usernames, File) """
        if ctx.author.guild_permissions.manage_roles:
            left_over = []
            successful = []
            await ctx.send("Reply with discord usernames (follow the format)")

            def check(m):
                return m.author.id == ctx.author.id

            message = await self.client.wait_for('message', check=check, timeout=120)
            if not message.author.bot:
                await ctx.send("on it :cat:")
                if message.attachments:
                    attachment = message.attachments[0]
                    with attachment.save() as file:
                        username_list = file
                else:
                    msg = message.content
                    username_list = msg.split('\n')
                for username in username_list:
                    username = username.rstrip()
                    try:
                        namez, id = username.split('#')
                        user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                    except:
                        user = None
                    if user == None:
                        left_over.append(username)
                    else:
                        await user.add_roles(role)
                        successful.append(username)
                wled = "**Successful**"
                for i in successful:
                    wled = wled + "\n" + i
                nwled = "**Not Found**"
                for i in left_over:
                    nwled = nwled + "\n" + i

                if 15 < len(wled) < 1900:
                    await message.channel.send(wled)
                if 14 < len(nwled) < 1900:
                    await message.channel.send(nwled)

                await ctx.send(f"Successfully done for {len(successful)} users")
                await ctx.send(f"Couldn't find {len(left_over)} users")

    @commands.command()
    async def ungib(self, ctx, role: discord.Role):
        """ Remove Roles to Given list of Usernames (Works Usernames, File) """
        if ctx.author.guild_permissions.manage_roles:
            left_over = []
            successful = []
            await ctx.send("Reply with discord usernames (follow the format)")

            def check(m):
                return m.author.id == ctx.author.id

            message = await self.client.wait_for('message', check=check, timeout=120)
            if not message.author.bot:
                await ctx.send("on it :cat:")
                if message.attachments:
                    attachment = message.attachments[0]
                    with attachment.save() as file:
                        username_list = file
                else:
                    msg = message.content
                    username_list = msg.split('\n')
                for username in username_list:
                    username = username.rstrip()
                    try:
                        namez, id = username.split('#')
                        user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                    except:
                        user = None
                    if user == None:
                        left_over.append(username)
                    else:
                        await user.remove_roles(role)
                        successful.append(username)
                wled = "**Successful**"
                for i in successful:
                    wled = wled + "\n" + i
                nwled = "**Not Found**"
                for i in left_over:
                    nwled = nwled + "\n" + i

                if 15 < len(wled) < 1900:
                    await message.channel.send(wled)
                if 14 < len(nwled) < 1900:
                    await message.channel.send(nwled)

                await ctx.send(f"Successfully done for {len(successful)} users")
                await ctx.send(f"Couldn't find {len(left_over)} users")

    @commands.command()
    async def kic(self, ctx):
        """ Remove Roles to Given list of Usernames (Works Usernames, File) """
        if ctx.author.guild_permissions.manage_roles:
            left_over = []
            successful = []
            await ctx.send("Reply with discord usernames (follow the format)")

            def check(m):
                return m.author.id == ctx.author.id

            message = await self.client.wait_for('message', check=check, timeout=120)
            if not message.author.bot:
                await ctx.send("on it :cat:")
                if message.attachments:
                    attachment = message.attachments[0]
                    with attachment.save() as file:
                        username_list = file
                else:
                    msg = message.content
                    username_list = msg.split('\n')
                for username in username_list:
                    username = username.rstrip()
                    try:
                        namez, id = username.split('#')
                        user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                    except:
                        user = None
                    if user == None:
                        left_over.append(username)
                    else:
                        await user.kick()
                        successful.append(username)
                wled = "**Successful**"
                for i in successful:
                    wled = wled + "\n" + i
                nwled = "**Not Found**"
                for i in left_over:
                    nwled = nwled + "\n" + i

                if 15 < len(wled) < 1900:
                    await message.channel.send(wled)
                if 14 < len(nwled) < 1900:
                    await message.channel.send(nwled)

                await ctx.send(f"Successfully done for {len(successful)} users")
                await ctx.send(f"Couldn't find {len(left_over)} users")
                
    @commands.command()
    async def dust(self, ctx, reason="None"):
        """ Remove Roles to Given list of Usernames (Works Usernames, File) """
        if ctx.author.guild_permissions.manage_roles:
            left_over = []
            successful = []
            await ctx.send("Reply with discord usernames (follow the format)")

            def check(m):
                return m.author.id == ctx.author.id

            message = await self.client.wait_for('message', check=check, timeout=120)
            if not message.author.bot:
                await ctx.send("on it :cat:")
                if message.attachments:
                    attachment = message.attachments[0]
                    with attachment.save() as file:
                        username_list = file
                else:
                    msg = message.content
                    username_list = msg.split('\n')
                for username in username_list:
                    username = username.rstrip()
                    try:
                        namez, id = username.split('#')
                        user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                    except:
                        user = None
                    if user == None:
                        left_over.append(username)
                    else:
                        await user.ban(reason=reason)
                        successful.append(username)
                wled = "**Successful**"
                for i in successful:
                    wled = wled + "\n" + i
                nwled = "**Not Found**"
                for i in left_over:
                    nwled = nwled + "\n" + i

                if 15 < len(wled) < 1900:
                    await message.channel.send(wled)
                if 14 < len(nwled) < 1900:
                    await message.channel.send(nwled)

                await ctx.send(f"Successfully done for {len(successful)} users")
                await ctx.send(f"Couldn't find {len(left_over)} users")

    @commands.command()
    async def assign(self, ctx, role: discord.Role):
        """ On the replied message it assigns roles to mentioned users """
        if ctx.message.reference:
            message = await ctx.fetch_message(ctx.message.reference.message_id)
        else:
            await ctx.send("Please reply to the message")
            message_id = 991908762992513064    # Stupid case
            message = await ctx.fetch_message(message_id)
        for user in message.mentions:
            await user.add_roles(role)

        await ctx.send("Done")

    @commands.command()
    async def list(self, ctx):
        """ On the replied message DMs the IDs and Usernames of mentioned Users """
        if ctx.message.reference:
            message = await ctx.fetch_message(ctx.message.reference.message_id)
        else:
            await ctx.send("Please reply to the message")
            message_id = 991908762992513064    # Again Stupid Case
            message = await ctx.fetch_message(message_id)

        author_list = []
        successful = []
        for user in message.mentions:
            author_list.append(user.name + "#" + user.discriminator)
            successful.append(str(user.id))

        msg = "**Usernames**\n"
        for user in author_list:
            msg = msg + user + "\n"
        await ctx.author.send(msg)
        msg = "**UserIDs**\n"
        for user_id in successful:
            msg = msg + user_id + "\n"
        await ctx.author.send(msg)
        await ctx.send(f"Check DM")

    @commands.command()
    async def get_wallets(self, ctx):
        channel = ctx.channel
        user_ids = []
        user_wallets = []
        user_names = []
        async for message in channel.history(limit=300):
            if message.content.startswith('bc') and message.author.id not in user_ids:
                user_ids.append(message.author.id)
                user_names.append(message.author.name + '#' + str(message.author.discriminator))
                user_wallets.append(message.content)
        user_ids.reverse()
        user_wallets.reverse()
        user_names.reverse()
        with open("results.csv", 'w', encoding='utf-8') as f:
            f.write(f"DiscordID,Username,Wallet\n")
            for i in range(len(user_ids)):
                f.write(f"{user_ids[i]},{user_names[i]},{user_wallets[i]}\n")

        file = discord.File("results.csv")
        await ctx.send(file=file, content=">.<")
        os.remove('results.csv')

    @commands.command()
    async def get_wallets_repeat(self, ctx):
        channel = ctx.channel
        user_ids = []
        user_wallets = []
        user_names = []
        async for message in channel.history(limit=300):
            if message.content.startswith('bc'):
                user_ids.append(message.author.id)
                user_names.append(message.author.name + '#' + str(message.author.discriminator))
                user_wallets.append(message.content)
        user_ids.reverse()
        user_wallets.reverse()
        user_names.reverse()
        with open("results.csv", 'w', encoding='utf-8') as f:
            f.write(f"DiscordID,Username,Wallet\n")
            for i in range(len(user_ids)):
                f.write(f"{user_ids[i]},{user_names[i]},{user_wallets[i]}\n")

        file = discord.File("results.csv")
        await ctx.send(file=file, content=">.<")
        os.remove('results.csv')


async def setup(client):
    await client.add_cog(Moderation(client))
