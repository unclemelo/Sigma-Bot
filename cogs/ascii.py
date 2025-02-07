import discord
from discord import app_commands
from discord.ext import commands

class AsciiGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="ascii", description="ASCII art commands")

    @app_commands.command(name="val", description="Generate ASCII art or perform actions based on choices")
    @app_commands.choices(
        text=[
            app_commands.Choice(name="-20rr", value="-20rr"),
            app_commands.Choice(name="-15zz", value="-15zz"),
            app_commands.Choice(name="-42xy", value="-42xy"),
        ]
    )
    async def val(self, interaction: discord.Interaction, text: str):
        if text == "-20rr":
            ascii_art = """\
――――――▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌――-- ▄▄██▌█ BEEP BEEP ―――――― ▄▄▄▌▐██▌█ -20rr delivery 
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌▀(@)▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀(@)(@)▀▀▘
"""
            await interaction.response.send_message(ascii_art)
#         elif text == "-15zz":
#             ascii_art_2 = """\
# -- ASCII Art for -15zz --
# (ASCII art or response for -15zz)
# """
#             await interaction.response.send_message(ascii_art_2)
#         elif text == "-42xy":
#             ascii_art_3 = """\
# -- ASCII Art for -42xy --
# (ASCII art or response for -42xy)
# """
#             await interaction.response.send_message(ascii_art_3)
        else:
            await interaction.response.send_message("Invalid choice!", ephemeral=True)

# Create a Cog to add the command
class Ascii(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.tree.add_command(AsciiGroup())  # Register the group command

async def setup(bot: commands.Bot):
    await bot.add_cog(Ascii(bot))
