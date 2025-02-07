import discord
from discord import app_commands
from discord.ext import commands
import random

class MyGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="game", description="Play different games")

    @app_commands.command(name="guess", description="Play the guessing game")
    async def guess(self, interaction: discord.Interaction):
        await interaction.response.send_message("Guess a number between 1 and 10!")

    @app_commands.command(name="rps", description="Play rock-paper-scissors")
    async def rps(self, interaction: discord.Interaction, choice: str):
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)

        if choice.lower() not in choices:
            await interaction.response.send_message("Invalid choice! Choose rock, paper, or scissors.")
            return

        result = "You win!" if (
            (choice == "rock" and bot_choice == "scissors") or
            (choice == "paper" and bot_choice == "rock") or
            (choice == "scissors" and bot_choice == "paper")
        ) else "You lose!" if choice != bot_choice else "It's a tie!"

        await interaction.response.send_message(f"You chose {choice}, I chose {bot_choice}. {result}")

class Game(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.tree.add_command(MyGroup())

async def setup(bot: commands.Bot):
    await bot.add_cog(Game(bot))