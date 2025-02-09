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
    "Janitor": {"pay_range": (10000, 20000), "cooldown": 50, "required_works": 0},
    "Cashier": {"pay_range": (15000, 30000), "cooldown": 100, "required_works": 20},
    "Construction Worker": {"pay_range": (30000, 60000), "cooldown": 150, "required_works": 50},
    "Software Engineer": {"pay_range": (80000, 150000), "cooldown": 200, "required_works": 100},
    "Doctor": {"pay_range": (150000, 300000), "cooldown": 300, "required_works": 300}
}

class Economy(commands.Cog):
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
            self.economy_data[user_id] = {"coins": 0, "job": "Janitor", "works_done": 0, "last_work_time": None, "last_daily": None}
        return self.economy_data[user_id]

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

        # Check if user can unlock a new job
        for new_job, details in JOBS.items():
            if user_data["works_done"] >= details["required_works"] and details["required_works"] > JOBS[job]["required_works"]:
                user_data["job"] = new_job
                await interaction.response.send_message(f"You've been promoted to **{new_job}**! 🎉\nYou earned ${pay}.")
                break
        else:
            await interaction.response.send_message(f"You earned ${pay} from your job as a **{job}**.")

        self.save_data()

    @app_commands.command(name="balance", description="Check your balance")
    async def balance(self, interaction: discord.Interaction):
        user_data = self.get_user_data(interaction.user.id)
        await interaction.response.send_message(f"💰 You have **${user_data['coins']}**.")

    @app_commands.command(name="leaderboard", description="Check the top earners")
    async def leaderboard(self, interaction: discord.Interaction):
        sorted_users = sorted(self.economy_data.items(), key=lambda x: x[1]["coins"], reverse=True)
        leaderboard_text = "\n".join([f"{i+1}. <@{user_id}> - ${data['coins']}" for i, (user_id, data) in enumerate(sorted_users[:10])])
        await interaction.response.send_message(f"🏆 **Leaderboard:**\n{leaderboard_text}")

    @app_commands.command(name="daily", description="Claim your daily coins!")
    async def daily(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)
        last_claim = user_data.get("last_daily")

        if last_claim:
            last_claim_date = datetime.fromisoformat(last_claim)
            if last_claim_date.date() == datetime.utcnow().date():
                await interaction.response.send_message("You've already claimed your daily reward today! Come back tomorrow.")
                return

        reward = 100
        user_data["coins"] += reward
        user_data["last_daily"] = datetime.utcnow().isoformat()
        self.save_data()
        await interaction.response.send_message(f"✅ You claimed your daily reward of **${reward}**!")

    @app_commands.command(name="shop", description="View the shop and buy items!")
    async def shop(self, interaction: discord.Interaction):
        items = {
            "Knife": 500,
            "Pistol": 15000,
            "Rifle": 500000,
            "Nuke": 999999999
        }
        shop_text = "\n".join([f"🔹 **{item}** - ${price}" for item, price in items.items()])
        await interaction.response.send_message(f"🛒 **Shop:**\n{shop_text}")

    @app_commands.command(name="buy", description="Buy an item from the shop")
    async def buy(self, interaction: discord.Interaction, item: str):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)

        shop_items = {
            "Knife": 500,
            "Pistol": 1500,
            "Rifle": 500000,
            "Nuke": 999999999
        }

        item = item.capitalize()
        if item not in shop_items:
            await interaction.response.send_message("That item is not available in the shop!")
            return

        price = shop_items[item]
        if user_data["coins"] < price:
            await interaction.response.send_message("You don't have enough money for that!")
            return

        user_data["coins"] -= price
        user_data.setdefault("inventory", []).append(item)
        self.save_data()
        await interaction.response.send_message(f"✅ You bought a **{item}** for **${price}**!")

    @app_commands.command(name="inventory", description="Check your inventory")
    async def inventory(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)
        inventory = user_data.get("inventory", [])

        if not inventory:
            await interaction.response.send_message("Your inventory is empty!")
        else:
            inventory_list = ", ".join(inventory)
            await interaction.response.send_message(f"👜 **Your Inventory:** {inventory_list}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
