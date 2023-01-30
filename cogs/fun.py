import asyncio
import os
import discord
import random
import requests
from discord.ext import commands
import json
from cogs.databasecog import Database
from cogs.utils import Utils

conf = open("./cogs/config.json")
config = json.load(conf)

# Ethos
ethos = config['guilds']['ethos']


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = Database(self.client)
        self.utils = Utils(self.client)

    @commands.command()
    async def say(self, ctx, *args):
        if self.utils.isValid(ctx.author):
            stc = ""
            for i in args:
                stc = stc + i + " "
            await ctx.send(stc)

    @commands.command()
    async def cat(self, ctx):
        if self.utils.isValid(ctx.author):
            headers = {
                "x-api-key": os.environ['CAT_API']
            }
            r = requests.get("https://api.thecatapi.com/v1/images/search/", headers=headers).content
            r = json.loads(r)
            await ctx.send(r[0]['url'])

    @commands.command()
    async def selfie(self, ctx):
        if self.utils.isValid(ctx.author):
            img_list = self.db.query().find_one({"_id": "selfie"})['selfie_list']
            await ctx.send(random.choice(img_list))

    @commands.command()
    async def join(self, ctx):
        """ Makes the bot join Rumble """
        if self.utils.isValid(ctx.author):
            async for message in ctx.channel.history(limit=200):
                if message.author.id == 693167035068317736:    # Rumble Bot ID
                    if len(message.reactions) != 0:
                        await message.add_reaction(message.reactions[0])
                        await ctx.send("RUMBLE TIMEEEE")

    @commands.command()
    async def unjoin(self, ctx):
        """ Makes the bot leave Rumble """
        if self.utils.isValid(ctx.author):
            async for message in ctx.channel.history(limit=200):
                if message.author.id == 693167035068317736:    # Rumble Bot ID
                    if len(message.reactions) != 0:
                        await message.remove_reaction(message.reactions[0], self.client.get_user(860904195279028245))
                        await ctx.send(":(((")

    @commands.command()
    async def rps(self, ctx):
        if self.utils.isValid(ctx.author):
            sent_msg = await self.utils.blue_embed(ctx.message, 'Rock, paper, scissors!')
            await sent_msg.add_reaction('✊')
            await sent_msg.add_reaction('✋')
            await sent_msg.add_reaction('✌')

            # wait for user reaction
            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ['✊', '✋', '✌']

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await ctx.message.reply('Sorry, you took too long to play.')
                return

            # determine winner
            choice = str(reaction.emoji)
            opponent_choice = random.choice(['✊', '✋', '✌'])
            if choice == '✊':
                if opponent_choice == '✋':
                    await self.utils.loser_embed(ctx, 'You lost! Paper beats rock. :) ')
                elif opponent_choice == '✌':
                    await self.utils.winner_embed(ctx, 'You won! Rock beats scissors. :( ')
                else:
                    await self.utils.draw_embed(ctx, 'It\'s a tie! :/')

            elif choice == '✋':
                if opponent_choice == '✌':
                    await self.utils.loser_embed(ctx, 'You lost! Scissors beats paper. :) ')
                elif opponent_choice == '✊':
                    await self.utils.winner_embed(ctx, 'You won! Paper beats rock. :( ')
                else:
                    await self.utils.draw_embed(ctx, 'It\'s a tie! :/')

            elif choice == '✌':
                if opponent_choice == '✊':
                    await self.utils.loser_embed(ctx, 'You lost! Rock beats scissors. :) ')
                elif opponent_choice == '✋':
                    await self.utils.winner_embed(ctx, 'You won! Scissors beats paper. :( ')
                else:
                    await self.utils.draw_embed(ctx, 'It\'s a tie! :/')

    @commands.command()
    async def catfact(self, ctx):
        if self.utils.isValid(ctx.author):
            r = requests.get("https://meowfacts.herokuapp.com/").content
            r = json.loads(r)
            fact = r['data'][0]
            await self.utils.pink_embed(ctx, fact)
            
    @commands.command()
    async def kill(self, ctx, user: discord.User):
        if self.utils.isValid(ctx.author):
            img_list = self.db.query().find_one({"_id": "kill"})['gif_list']
            embed = discord.Embed(title=f"**{ctx.author.name} killed {user.name}**", description=f"{user.mention} was killed. *No Way ;;;*", colour=discord.Colour.red())
            embed.set_image(url=f"{random.choice(img_list)}")
            await ctx.send(embed=embed)

    @commands.command()
    async def tickle(self, ctx, user: discord.User):
        if self.utils.isValid(ctx.author):
            embed = discord.Embed(title=f"**{user.name} has been tickled!**", description=f"{ctx.author.mention} tickles {user.mention} *nyaa*",
                                  colour=discord.Colour.magenta())
            embed.set_image(url=f"https://cdn.nekos.life/tickle/tickle_{str(random.choice(list(range(1,21)))).zfill(3)}.gif")
            await ctx.send(embed=embed)            


async def setup(client):
    await client.add_cog(Fun(client))
