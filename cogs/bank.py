import discord
from discord import app_commands
from discord.ext import commands
import json
import os

COINS_FILE = "economy.json"

class Bank(commands.Cog):
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
            self.economy_data[user_id] = {
                "coins": 0, "bank": 0, "bank_limit": 50000,  # Default bank limit
                "job": "Janitor", "works_done": 0, "last_work_time": None, "last_daily": None
            }
        return self.economy_data[user_id]

    @app_commands.command(name="deposit", description="Deposit money into the bank")
    async def deposit(self, interaction: discord.Interaction, amount: int):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)

        if amount <= 0:
            await interaction.response.send_message("❌ You can't deposit a negative or zero amount.")
            return

        if user_data["coins"] < amount:
            await interaction.response.send_message("❌ You don't have enough money to deposit that much.")
            return

        if user_data["bank"] + amount > user_data["bank_limit"]:
            await interaction.response.send_message("❌ You don't have enough bank space! Upgrade your bank to deposit more.")
            return

        user_data["coins"] -= amount
        user_data["bank"] += amount
        self.save_data()

        await interaction.response.send_message(f"✅ You deposited **${amount}** into your bank. Your new bank balance is **${user_data['bank']}**.")

    @app_commands.command(name="bank_balance", description="Check your bank balance")
    async def bank_balance(self, interaction: discord.Interaction):
        user_data = self.get_user_data(interaction.user.id)
        await interaction.response.send_message(f"🏦 **Bank Balance:** ${user_data['bank']} / ${user_data['bank_limit']}")

    @app_commands.command(name="upgrade_bank", description="Upgrade your bank to store more money")
    async def upgrade_bank(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)

        upgrade_cost = user_data["bank_limit"] // 2  # Upgrading costs 50% of current limit
        new_limit = user_data["bank_limit"] + 50000  # Increase bank limit by 50K

        if user_data["coins"] < upgrade_cost:
            await interaction.response.send_message(f"❌ You need **${upgrade_cost}** to upgrade your bank!")
            return

        user_data["coins"] -= upgrade_cost
        user_data["bank_limit"] = new_limit
        self.save_data()

        await interaction.response.send_message(f"✅ You upgraded your bank! Your new limit is **${new_limit}**.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Bank(bot))
