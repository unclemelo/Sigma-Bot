import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os

COINS_FILE = "economy.json"

class Robbery(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
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
        with open(COINS_FILE, "w") as f:
            json.dump(self.economy_data, f, indent=4)

    def get_user_data(self, user_id):
        user_id = str(user_id)
        if user_id not in self.economy_data:
            self.economy_data[user_id] = {"coins": 0, "bank": 0, "inventory": []}
        return self.economy_data[user_id]

    @app_commands.command(name="rob", description="Attempt to rob another player!")
    async def rob(self, interaction: discord.Interaction, target: discord.User):
        user_id = str(interaction.user.id)
        target_id = str(target.id)
        
        if user_id == target_id:
            await interaction.response.send_message("❌ You can't rob yourself!")
            return
        
        user_data = self.get_user_data(user_id)
        target_data = self.get_user_data(target_id)
        
        if target_data["coins"] <= 0:
            await interaction.response.send_message(f"❌ {target.mention} has no money in their wallet to rob!")
            return
        
        rob_success = random.randint(1, 100) <= 50  # 50% chance of success
        if rob_success:
            stolen_amount = random.randint(1, int(target_data["coins"] * 0.5))
            target_data["coins"] -= stolen_amount
            user_data["coins"] += stolen_amount
            self.save_data()
            await interaction.response.send_message(f"💰 You successfully robbed **${stolen_amount}** from {target.mention}!")
        else:
            fine = random.randint(1, 1000)
            user_data["coins"] = max(0, user_data["coins"] - fine)
            self.save_data()
            await interaction.response.send_message(f"🚓 You got caught and lost **${fine}** as a penalty!")
    
    @app_commands.command(name="heist", description="Attempt to rob a bank (requires a rifle)")
    async def heist(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)
        
        if "Rifle" not in user_data.get("inventory", []):
            await interaction.response.send_message("❌ You need a **Rifle** to rob a bank!")
            return
        
        heist_success = random.randint(1, 100) <= 40  # 40% chance of success
        if heist_success:
            reward = random.randint(100000, 500000)
            user_data["coins"] += reward
            self.save_data()
            await interaction.response.send_message(f"💰 You successfully robbed the bank and got **${reward}**!")
        else:
            loss = random.randint(50000, 200000)
            user_data["coins"] = max(0, user_data["coins"] - loss)
            self.save_data()
            await interaction.response.send_message(f"🚔 The police caught you! You lost **${loss}** trying to rob the bank.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Robbery(bot))
