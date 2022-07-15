import nextcord
import random
from nextcord.ext import commands

punching_gifs = ["https://tenor.com/bV97I.gif"]
  punching_names = ['Pass Him Down!']


class ActionGifs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pass(self, ctx: commands.Context,):
        embed = nextcord.Embed(
            colour=nextcord.Colour(0xCE3011),
            description=f"{(random.choice(punching_names))}"

        )
        embed.set_image(url=(random.choice(punching_gifs)))

        await ctx.send(embed=embed)

    
