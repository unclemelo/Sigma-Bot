import random
import asyncio
from discord import app_commands
from discord.ext import commands


class Guess(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="guess", description="the guess game")
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long it was {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send(f'Oops. It is actually {answer}.')


async def setup(bot: commands.Bot):
    await bot.add_cog(Guess(bot))


# class MyClient(discord.Client):
#     async def on_message(self, message):
#         # we do not want the bot to reply to itself
#         if message.author.id == self.user.id:
#             return
#
#         if message.content.startswith('$guess'):
#             await message.channel.send('Guess a number between 1 and 10.')
#
#             def is_correct(m):
#                 return m.author == message.author and m.content.isdigit()
#
#             answer = random.randint(1, 10)
#
#             try:
#                 guess = await self.wait_for('message', check=is_correct, timeout=5.0)
#             except asyncio.TimeoutError:
#                 return await message.channel.send(f'Sorry, you took too long it was {answer}.')
#
#             if int(guess.content) == answer:
#                 await message.channel.send('You are right!')
#             else:
#                 await message.channel.send(f'Oops. It is actually {answer}.')

