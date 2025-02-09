import random
import discord
from discord import app_commands
from functools import wraps
from discord.ext import commands

## Developer IDs ##
devs = {1268070879598870601, 1331452332688543815}  ## Replace with all the discord ids of bot Admins
###################

def is_dev():
    """Decorator to restrict commands to developers."""

    def predicate(func):
        @wraps(func)
        async def wrapper(self, interaction: discord.Interaction, *args, **kwargs):
            if interaction.user.id in self.devs:
                return await func(self, interaction, *args, **kwargs)
            await interaction.response.send_message(
                "This command is restricted to certain people.", ephemeral=True
            )

        return wrapper

    return predicate


class kaustinQuote(commands.Cog):
    """Cog for managing system-level commands like restarting and updating the bot."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.devs = devs

    @app_commands.command(name="kaustin", description="gives a weird ass quote that austin and kanya said at some point.")
    @is_dev()
    async def kaustin_quote(self, interaction: discord.Interaction):
        quotes = ['"Wait was ur cube white or black on the inside" - Kanya 2025',
                  '"and lube 😉" - Austin 2025',
                  '"YOU GOT MARRIED TO A CUBE?, is that why u need the lube?" Kanya 2025',
                  '"You could like sit with it for hours" - Kanya 2025'
                  ]

        quote = random.choice(quotes)
        await interaction.response.send_message(quote)


async def setup(bot: commands.Bot):
    """Adds the Updater cog to the bot."""
    await bot.add_cog(SanvikaQuote(bot))