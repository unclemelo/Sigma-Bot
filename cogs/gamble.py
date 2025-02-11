import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

COINS_FILE = "economy.json"

class Gamble(commands.Cog):
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

    @app_commands.command(name="coinflip", description="Bet your coins on a coin flip")
    async def coinflip(self, interaction: discord.Interaction, bet: int, choice: str):
        try:
            await interaction.response.defer()
            user_id = str(interaction.user.id)
            user_data = self.get_user_data(user_id)

            if bet <= 0:
                await interaction.followup.send("❌ You must bet a positive amount of coins.")
                return

            if user_data["coins"] < bet:
                await interaction.followup.send("❌ You don't have enough coins to place this bet.")
                return

            choice = choice.lower()
            if choice not in ["heads", "tails"]:
                await interaction.followup.send("❌ Invalid choice! Choose 'Heads' or 'Tails'.")
                return

            result = random.choice(["heads", "tails"])
            if choice == result:
                winnings = bet * 2
                user_data["coins"] += winnings
                await interaction.followup.send(f"🎉 The coin landed on **{result}**! You won **${winnings}**!")
            else:
                user_data["coins"] -= bet
                await interaction.followup.send(f"😢 The coin landed on **{result}**. You lost **${bet}**.")
            
            self.save_data()
        except Exception as e:
            logger.error(f"Error in coinflip: {e}")
            await interaction.followup.send("An error occurred while processing your request. Please try again.")

    @app_commands.command(name="dice", description="Bet on a dice roll (1-6)")
    async def dice(self, interaction: discord.Interaction, bet: int, guess: int):
        try:
            await interaction.response.defer()
            user_id = str(interaction.user.id)
            user_data = self.get_user_data(user_id)

            if bet <= 0:
                await interaction.followup.send("❌ You must bet a positive amount of coins.")
                return

            if user_data["coins"] < bet:
                await interaction.followup.send("❌ You don't have enough coins to place this bet.")
                return

            if guess < 1 or guess > 6:
                await interaction.followup.send("❌ Invalid guess! Choose a number between 1 and 6.")
                return

            roll = random.randint(1, 6)
            if guess == roll:
                winnings = bet * 6
                user_data["coins"] += winnings
                await interaction.followup.send(f"🎲 The dice rolled **{roll}**! You won **${winnings}**!")
            else:
                user_data["coins"] -= bet
                await interaction.followup.send(f"😢 The dice rolled **{roll}**. You lost **${bet}**.")
            
            self.save_data()
        except Exception as e:
            logger.error(f"Error in dice: {e}")
            await interaction.followup.send("An error occurred while processing your request. Please try again.")

    @app_commands.command(name="guess", description="Play the guessing game with coins")
    async def guess(self, interaction: discord.Interaction, bet: int):
        try:
            await interaction.response.defer()
            user_id = str(interaction.user.id)
            user_data = self.get_user_data(user_id)

            if bet <= 0:
                await interaction.followup.send("❌ You must bet a positive amount of coins.")
                return

            if user_data["coins"] < bet:
                await interaction.followup.send("❌ You don't have enough coins to place this bet.")
                return

            number = random.randint(1, 10)
            await interaction.followup.send(f"Guess a number between 1 and 10! Bet: ${bet}. Type your guess in the chat.")

            def check(msg):
                return msg.author == interaction.user and msg.channel == interaction.channel and msg.content.isdigit()

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=15)
                guess = int(msg.content)

                if guess == number:
                    winnings = bet * 2
                    user_data["coins"] += winnings
                    await interaction.followup.send(f"🎉 Correct! The number was {number}. You won **${winnings}**!")
                else:
                    user_data["coins"] -= bet
                    await interaction.followup.send(f"❌ Wrong! The correct number was {number}. You lost **${bet}**.")
            except TimeoutError:
                await interaction.followup.send("⏳ Time's up! You didn't guess in time. You lost your bet.")
            except Exception as e:
                logger.error(f"Error in guess: {e}")
                await interaction.followup.send("An unexpected error occurred during the guess game.")
            
            self.save_data()
        except Exception as e:
            logger.error(f"Error in guess: {e}")
            await interaction.followup.send("An error occurred while setting up the game. Please try again.")

    @app_commands.command(name="rockpaperscissors", description="Play rock-paper-scissors with coins")
    async def rps(self, interaction: discord.Interaction, bet: int, choice: str):
        try:
            await interaction.response.defer()
            user_id = str(interaction.user.id)
            user_data = self.get_user_data(user_id)

            if bet <= 0:
                await interaction.followup.send("❌ You must bet a positive amount of coins.")
                return

            if user_data["coins"] < bet:
                await interaction.followup.send("❌ You don't have enough coins to place this bet.")
                return

            choices = ["rock", "paper", "scissors"]
            bot_choice = random.choice(choices)

            if choice.lower() not in choices:
                await interaction.followup.send("Invalid choice! Choose rock, paper, or scissors.")
                return

            result = "You win!" if (
                    (choice == "rock" and bot_choice == "scissors") or
                    (choice == "paper" and bot_choice == "rock") or
                    (choice == "scissors" and bot_choice == "paper")
            ) else "You lose!" if choice != bot_choice else "It's a tie!"

            if result == "You win!":
                winnings = bet * 2
                user_data["coins"] += winnings
                await interaction.followup.send(f"You chose {choice}, I chose {bot_choice}. {result} You won **${winnings}**!")
            elif result == "You lose!":
                user_data["coins"] -= bet
                await interaction.followup.send(f"You chose {choice}, I chose {bot_choice}. {result} You lost **${bet}**.")
            else:  # It's a tie
                await interaction.followup.send(f"You chose {choice}, I chose {bot_choice}. {result}. Your bet of **${bet}** is returned.")
            
            self.save_data()
        except Exception as e:
            logger.error(f"Error in rps: {e}")
            await interaction.followup.send("An error occurred while processing your request. Please try again.")

    @app_commands.command(name="blackjack", description="Play Blackjack with coins")
    async def blackjack(self, interaction: discord.Interaction, bet: int):
        try:
            await interaction.response.defer()
            user_id = str(interaction.user.id)
            user_data = self.get_user_data(user_id)

            if bet <= 0:
                await interaction.followup.send("❌ You must bet a positive amount of coins.")
                return

            if user_data["coins"] < bet:
                await interaction.followup.send("❌ You don't have enough coins to place this bet.")
                return

            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # Simplified deck with Aces as 11
            random.shuffle(deck)

            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]

            def hand_value(hand):
                # Adjust Aces value
                value = sum(hand)
                ace_count = hand.count(11)
                while value > 21 and ace_count:
                    value -= 10
                    ace_count -= 1
                return value

            async def create_embed(player_hand, dealer_hand, show_dealer=False):
                embed = discord.Embed(title="Blackjack", color=discord.Color.green())
                
                player_cards = [f"cards/{card if card != 11 else 'A'}.png" for card in player_hand]
                dealer_cards = [f"cards/{dealer_hand[0] if dealer_hand[0] != 11 else 'A'}.png"] if not show_dealer else [f"cards/{card if card != 11 else 'A'}.png" for card in dealer_hand]
                
                embed.add_field(name="Your Hand", value=f"Value: {hand_value(player_hand)}", inline=False)
                embed.set_image(url=player_cards[0])  # Placeholder for showing one card image
                
                if show_dealer:
                    embed.add_field(name="Dealer's Hand", value=f"Value: {hand_value(dealer_hand)}", inline=False)
                    embed.set_thumbnail(url=dealer_cards[0])  # Placeholder for dealer's card
                else:
                    embed.add_field(name="Dealer's Hand", value="Value: ?", inline=False)
                    embed.set_thumbnail(url="cards/back.png")  # Assuming you have a back card image

                return embed

            class BlackjackView(discord.ui.View):
                def __init__(self, player_hand, dealer_hand, deck, bet, user_data, interaction):
                    super().__init__()
                    self.player_hand = player_hand
                    self.dealer_hand = dealer_hand
                    self.deck = deck
                    self.bet = bet
                    self.user_data = user_data
                    self.interaction = interaction

                @discord.ui.button(label="Hit", style=discord.ButtonStyle.green)
                async def hit(self, button: discord.ui.Button, interaction: discord.Interaction):
                    new_card = self.deck.pop()
                    self.player_hand.append(new_card)
                    if hand_value(self.player_hand) > 21:
                        await self.end_game(interaction, "bust")
                        return

                    embed = await create_embed(self.player_hand, self.dealer_hand)
                    await interaction.response.edit_message(embed=embed, view=self)

                @discord.ui.button(label="Stand", style=discord.ButtonStyle.red)
                async def stand(self, button: discord.ui.Button, interaction: discord.Interaction):
                    await self.end_game(interaction, "stand")

                async def end_game(self, interaction, reason):
                    if reason == "bust":
                        message = f"Bust! You lost **${self.bet}**."
                        self.user_data["coins"] -= self.bet
                    else:
                        while hand_value(self.dealer_hand) < 17:
                            new_card = self.deck.pop()
                            self.dealer_hand.append(new_card)
                            if hand_value(self.dealer_hand) > 21:
                                break

                        dealer_value = hand_value(self.dealer_hand)
                        player_value = hand_value(self.player_hand)

                        if dealer_value > 21:
                            message = f"Dealer busts! You win **${self.bet * 2}**!"
                            self.user_data["coins"] += self.bet * 2
                        elif player_value > dealer_value:
                            message = f"You win! You won **${self.bet * 2}**!"
                            self.user_data["coins"] += self.bet * 2
                        elif player_value < dealer_value:
                            message = f"Dealer wins! You lost **${self.bet}**."
                            self.user_data["coins"] -= self.bet
                        else:
                            message = "It's a push! Your bet is returned."

                    embed = await create_embed(self.player_hand, self.dealer_hand, show_dealer=True)
                    embed.description = message
                    await interaction.response.edit_message(embed=embed, view=None)
                    self.save_data()

            initial_embed = await create_embed(player_hand, dealer_hand)
            view = BlackjackView(player_hand, dealer_hand, deck, bet, user_data, interaction)
            await interaction.followup.send(embed=initial_embed, view=view)
        except Exception as e:
            logger.error(f"Error in blackjack: {e}")
            await interaction.followup.send("An error occurred while processing your blackjack game. Please try again.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Gamble(bot))