import discord
from discord import app_commands
from discord.ext import commands
from functools import wraps
import random

## Developer IDs ##
devs = {1239123901239102380129381}       ## Replace with all the discord ids of bot Admins
###################

def is_dev():
    """Decorator to restrict commands to developers."""
    def predicate(func):
        @wraps(func)
        async def wrapper(self, interaction: discord.Interaction, *args, **kwargs):
            if interaction.user.id in self.devs:
                return await func(self, interaction, *args, **kwargs)
            await interaction.response.send_message(
                "This command is restricted to developers.", ephemeral=True
            )
        return wrapper
    return predicate


class quotes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.devs = devs



    @app_commands.command(name="quote", description="The quote command")
    async def on_message(devs, interaction: discord.Interaction):
        quotes = ['"ima bust all over tavisha" - Sanvika 2025',
                  '"ima kidnap you and take you to china" - Sanvika 2025',
                  '"the only people allowed to touch you are yizhi and me" - Sanvika 2025',
                  '"and then once it was over i gave him the head" - Sanvika 2025',
                  '"so i just gave him the body" - Sanvika 2025',
                  '"yea yall should post that on ur of" - Sanvika 2025',
                  '"i am diddys number one customer" - Sanvika 2025',
                  '"ima oil up rq" - Sanvika 2024 & 2025',
                  '"OH MY GODDDDD" - Sanvika 2025',
                  '"i bet u cum when u see yizhi" - Sanvika 2025',
                  '"plus im alr hard and i cant be both at the same time yk" - Sanvika 2025',
                  '"i know your obsessed with both bjs and blackjack" - Sanvika 2025',
                  '"yeah nuts for life bro" - Sanvika 2025'
                  ]

        quote = random.choice(quotes)

        await interaction.response.send_message(quote)





async def setup(bot: commands.Bot):
    await bot.add_cog(quotes(bot))