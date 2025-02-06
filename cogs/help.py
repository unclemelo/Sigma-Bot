import discord
from discord import app_commands
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="The help command")
    async def cmdname(self, interaction: discord.Interaction):
        await interaction.response.send_message("help:\n\b                    Commands for Sigma Bot:\n/help = launches the help menu\n/guess = starts a game where you need to try and guess a number from 1 - 10\n\b                    Features of Sigma bot:\nWhen a message is deleted, it shows what that message is\nWhen a message is editied, it shows what that message was and what it changed to")


async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))


# class MyClient(discord.Client):
#     async def on_message(self, message):
#         if message.content.startswith('$help'):
#             await message.channel.send('                    Commands for Sigma Bot:')
#             await message.channel.send('/help = launches the help menu')
#             await message.channel.send('$guess = starts a game where you need to try and guess a number from 1 - 10')
#             await message.channel.send('                    Features of Sigma bot:')
#             await message.channel.send('When a message is deleted, it shows what that message is')
#             await message.channel.send(
#                 'When a message is editied, it shows what that message was and what it changed to')
