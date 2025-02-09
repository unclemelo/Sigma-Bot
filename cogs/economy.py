import discord
from discord import app_commands
from discord.ext import commands
import random
import asyncio
import json
import os
from datetime import datetime, timedelta

COINS_FILE = "economy.json"

JOBS = {
    "Janitor": {"pay_range": (10000, 20000), "cooldown": 9000, "required_works": 0},
    "Cashier": {"pay_range": (15000, 30000), "cooldown": 10000, "required_works": 20},
    "Construction Worker": {"pay_range": (30000, 60000), "cooldown": 28999, "required_works": 50},
    "Software Engineer": {"pay_range": (80000, 150000), "cooldown": 40000, "required_works": 100},
    "Doctor": {"pay_range": (150000, 3000000), "cooldown": 50000, "required_works": 300}
}

class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        """Load economy data from a JSON file."""
        if os.path.exists(COINS_FILE):
            try:
                with open(COINS_FILE, "r") as f:
                    content = f.read().strip()
                    self.economy_data = json.loads(content) if content else {}
            except json.JSONDecodeError:
                print("Error: economy.json is corrupted. Resetting file.")
                self.economy_data = {}
                self.save_data()
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
            self.economy_data[user_id] = {"coins": 0, "bank": 0, "job": "Janitor", "works_done": 0, "last_work_time": None, "last_daily": None}
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

    @app_commands.command(name="work", description="Work a job to earn coins")
    async def work(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)
        job = user_data["job"]

        last_work_time = user_data.get("last_work_time")
        cooldown = JOBS[job]["cooldown"]

        if last_work_time:
            elapsed_time = (datetime.utcnow() - datetime.fromisoformat(last_work_time)).total_seconds()
            if elapsed_time < cooldown:
                remaining_time = cooldown - elapsed_time
                await interaction.response.send_message(f"You're still working! Wait {int(remaining_time)} seconds.")
                return

        pay = random.randint(*JOBS[job]["pay_range"])
        user_data["coins"] += pay
        user_data["works_done"] += 1
        user_data["last_work_time"] = datetime.utcnow().isoformat()

        for new_job, details in JOBS.items():
            if user_data["works_done"] >= details["required_works"] and details["required_works"] > JOBS[job]["required_works"]:
                user_data["job"] = new_job
                await interaction.response.send_message(f"You've been promoted to **{new_job}**! 🎉\nYou earned ${pay}.")
                break
        else:
            await interaction.response.send_message(f"You earned ${pay} from your job as a **{job}**.")

        self.save_data()

async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
