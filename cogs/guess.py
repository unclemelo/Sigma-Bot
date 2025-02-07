import random
import asyncio
import discord
from discord import app_commands
from discord.ext import commands

class Guess(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="guess", description="Guess a number between 1 and 10")
    async def guess(self, interaction: discord.Interaction):
        answer = random.randint(1, 10)

        await interaction.response.send_message("Guess a number between 1 and 10.")

        def is_correct(m: discord.Message):
            return m.author == interaction.user and m.content.isdigit()

        try:
            guess = await self.bot.wait_for("message", check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await interaction.followup.send(f"Sorry, you took too long! The answer was {answer}.")

        if int(guess.content) == answer:
            await interaction.followup.send("You are right!")
        else:
            await interaction.followup.send(f"Oops! The correct answer was {answer}.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Guess(bot))
