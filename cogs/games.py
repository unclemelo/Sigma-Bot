import discord
from discord import app_commands
from discord.ext import commands
import random


class Games(app_commands.Group):
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

    @app_commands.command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, interaction: discord.Interaction):
        result = random.choice(["Heads", "Tails"])
        await interaction.response.send_message(f"The coin landed on {result}!")

    @app_commands.command(name="tictactoe", description="Play Tic Tac Toe!")
    async def tictactoe(self, interaction: discord.Interaction):
        await interaction.response.send_message("Tic Tac Toe is a bit more involved. You will play against the bot!")

        # For simplicity, we're going to implement a 3x3 board
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        def print_board():
            return f"""
            {board[0]} | {board[1]} | {board[2]}
            ---------
            {board[3]} | {board[4]} | {board[5]}
            ---------
            {board[6]} | {board[7]} | {board[8]}
            """

        await interaction.response.send_message(print_board())

        # The bot will play as 'O' and the user as 'X'
        def check_win(symbol):
            for (a, b, c) in win_conditions:
                if board[a] == board[b] == board[c] == symbol:
                    return True
            return False

        async def make_move(symbol):
            # Bot's move: choose an empty spot
            available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
            move = random.choice(available_moves)
            board[move] = symbol
            if check_win(symbol):
                return True, f"Bot (O) wins! {print_board()}"
            return False, print_board()

        # Example of a turn-based game loop:
        user_turn = True
        while True:
            if user_turn:
                await interaction.response.send_message(f"Your turn! Choose a number between 1-9 for your move.")
                # Assuming user input here, you can integrate logic to wait for input
                # For simplicity, I'll proceed to the bot move directly
                user_turn = False
            else:
                bot_wins, board_state = await make_move('O')
                await interaction.response.send_message(board_state)
                if bot_wins:
                    break
                user_turn = True

    @app_commands.command(name="dice", description="Roll a dice!")
    async def dice(self, interaction: discord.Interaction):
        result = random.randint(1, 6)
        await interaction.response.send_message(f"You rolled a {result}!")


class Game(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.tree.add_command(Games())  # Register the game group


async def setup(bot: commands.Bot):
    await bot.add_cog(Game(bot))
