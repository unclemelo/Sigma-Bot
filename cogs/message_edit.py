import discord
from discord import app_commands
from discord.ext import commands


class msgEdit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)


async def setup(bot: commands.Bot):
    await bot.add_cog(msgEdit(bot))
