import discord
from discord import app_commands
from discord.ext import commands


class msgDelete(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

async def setup(bot: commands.Bot):
    await bot.add_cog(msgDelete(bot))
