import discord
from discord import app_commands
from discord.ext import commands
import json
import os

COINS_FILE = "economy.json"

class Deposit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        """Load economy data from a JSON file."""
        if os.path.exists(COINS_FILE):
            with open(COINS_FILE, "r") as f:
                self.economy_data = json.load(f)
        else:
            self.economy_data = {}

    def save_data(self):
        """Save economy data to a JSON file."""
        with open(COINS_FILE, "w") as f:
            json.dump(self.economy_data, f, indent=4)

    def get_user_data(self, user_id):
        """Retrieve user data or create default if missing."""
        user_id = str(user_id)
        if user_id not in self.economy_data:
            self.economy_data[user_id] = {"coins": 0, "bank": 0}
        return self.economy_data[user_id]

    @app_commands.command(name="deposit", description="Deposit money into your bank")
    async def deposit(self, interaction: discord.Interaction, amount: int):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)

        if amount <= 0:
            await interaction.response.send_message("❌ You can't deposit a negative or zero amount.")
            return

        if user_data["coins"] < amount:
            await interaction.response.send_message("❌ You don't have enough money to deposit that much.")
            return

        user_data["coins"] -= amount
        user_data["bank"] += amount
        self.save_data()

        await interaction.response.send_message(f"✅ You deposited **${amount}** into your bank. Your new bank balance is **${user_data['bank']}**.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Deposit(bot))
