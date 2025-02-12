import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
import logging

COINS_FILE = "economy.json"

class Blackjack(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        if os.path.exists(COINS_FILE):
            with open(COINS_FILE, "r") as f:
                content = f.read().strip()
                self.economy_data = json.loads(content) if content else {}
        else:
            self.economy_data = {}

    def save_data(self):
        with open(COINS_FILE, "w") as f:
            json.dump(self.economy_data, f, indent=4)

    def get_user_data(self, user_id):
        user_id = str(user_id)
        if user_id not in self.economy_data:
            self.economy_data[user_id] = {"coins": 0, "bank": 0}
        return self.economy_data[user_id]

    def draw_card(self):
        """Draws a card, Ace is counted as 11 by default."""
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10s include J, Q, K
        return random.choice(cards)

    def calculate_hand(self, hand):
        """Calculate the best value of a blackjack hand."""
        total = sum(hand)
        aces = hand.count(11)

        while total > 21 and aces > 0:
            total -= 10  # Convert an Ace from 11 to 1
            aces -= 1

        return total

    @app_commands.command(name="blackjack", description="Play a game of Blackjack!")
    async def blackjack(self, interaction: discord.Interaction, bet: int):
        user_id = str(interaction.user.id)
        user_data = self.get_user_data(user_id)

        if bet <= 0:
            await interaction.response.send_message("❌ You must bet a positive amount.")
            return

        if user_data["coins"] < bet:
            await interaction.response.send_message("❌ You don't have enough coins to place that bet.")
            return

        # Initial deal
        player_hand = [self.draw_card(), self.draw_card()]
        dealer_hand = [self.draw_card(), self.draw_card()]

        await interaction.response.send_message(
            f"🃏 **Blackjack!** You bet **${bet}**\n"
            f"Your hand: {player_hand} (Total: {self.calculate_hand(player_hand)})\n"
            f"Dealer's hand: [{dealer_hand[0]}, ?]"
        )

        while self.calculate_hand(player_hand) < 21:
            await interaction.channel.send("Type `hit` to draw a card or `stand` to end your turn.")

            def check(msg):
                return msg.author == interaction.user and msg.channel == interaction.channel and msg.content.lower() in ["hit", "stand"]

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30)
                if msg.content.lower() == "hit":
                    player_hand.append(self.draw_card())
                    await interaction.channel.send(f"Your hand: {player_hand} (Total: {self.calculate_hand(player_hand)})")
                    if self.calculate_hand(player_hand) > 21:
                        await interaction.channel.send("💥 You busted! You lose.")
                        user_data["coins"] -= bet
                        self.save_data()
                        return
                else:
                    break
            except:
                await interaction.channel.send("⏳ Time's up! You automatically stand.")
                break

        # Dealer's turn
        while self.calculate_hand(dealer_hand) < 17:
            dealer_hand.append(self.draw_card())

        dealer_total = self.calculate_hand(dealer_hand)
        player_total = self.calculate_hand(player_hand)

        await interaction.channel.send(f"Dealer's final hand: {dealer_hand} (Total: {dealer_total})")
        
        if dealer_total > 21 or player_total > dealer_total:
            await interaction.channel.send(f"🎉 You win **${bet}**!")
            user_data["coins"] += bet
        elif player_total < dealer_total:
            await interaction.channel.send(f"❌ You lose **${bet}**!")
            user_data["coins"] -= bet
        else:
            await interaction.channel.send("🤝 It's a tie! Your bet is returned.")

        self.save_data()

async def setup(bot: commands.Bot):
    await bot.add_cog(Blackjack(bot))
