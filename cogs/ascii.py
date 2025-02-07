import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

class AsciiGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="ascii", description="ASCII art commands")

    @app_commands.command(name="val", description="Generate ASCII art to paste into val chat")
    @app_commands.choices(
        text=[
            app_commands.Choice(name="-20rr", value="-20rr"),
            app_commands.Choice(name="uninstall", value="uninstall"),
            app_commands.Choice(name="middlefinger", value="middlefinger"),
            app_commands.Choice(name="nerd", value="nerd"),
            app_commands.Choice(name="dontshoot", value="dontshoot"),
            app_commands.Choice(name="nice", value="nice"),
            app_commands.Choice(name="ggwp", value="ggwp"),
            app_commands.Choice(name="banhammer", value="banhammer"),
            app_commands.Choice(name="afk", value="afk"),
            app_commands.Choice(name="urmom", value="urmom"),
            app_commands.Choice(name="hmmm", value="hmmm"),
            app_commands.Choice(name="lol", value="lol"),
            app_commands.Choice(name="ace", value="ace"),
        ]
    )
    async def val(self, interaction: discord.Interaction, text: str):
        if text == "-20rr":
            ascii_art = """\
――――――▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌――-- ▄▄██▌█ BEEP BEEP ―――――― ▄▄▄▌▐██▌█ -20rr delivery ███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌▀(@)▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀(@)(@)▀▀▘
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "uninstall":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░UNINSTALLING░VALORANT░░░░░░░░░░░░░▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢░░░░░░░░░░░░░╭━╮╭━╮╭╮░╱░░░░░░░░░░░░░░░░╰━┫╰━┫╰╯╱╭╮░░░░░░░░░░░░░░░╰━╯╰━╯░╱░╰╯░░░░░░░░░░░░░░░░░COMPLETE░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "middlefinger":
            ascii_art = """\
▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▀▀█████▀▀██▒▒▒▒▒▒▒▒▒▒▒▒█████▄███▄█████▒▒▒▒▒█▒▒▒▒▐██░░░█████░░░██▌▒▒▒▒█▒▒▒▒▐██■░░█████■░░██▌▒▒▒▒█▒▒▒▒▐███████████████▌▒▒▒███▒▒▒▐███████████████▌▒▒▐███▒▒▒▐████▀▀▀▀▀▀▀████▌▒▒▐███▌▒▒▐███▌■■■■■■■▐███▌▒▒▒███▌▒▒▒███▌■■■■■■■▐███▒▒▒▒▒█████▌▒███▄▄▄▄▄▄▄███▒▒▒▒▒▒▒█████▒▒███████████▒▒▒
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "nerd":
            ascii_art = """\
────────────████████────── ───────────██████████───── ──────────█▄▄▄████▄▄▄█──── ─────▄───█░░░░░██░░░░░█─── ─────█──░░░▓■▓░░░░▓■▓░░░── ─────█──▐█░▓▓▓░██░▓▓▓░█▌── ─────█──▐██░░░████░░░██▌── ─────█──▐█▛██████████▛█▌── ──▌▌▌▄▄──██▚████████▞██─── ──▌▌▌▀█──████▀████▀████─── ──▄▄▄██───████▄■■▄████──── ──▜███▛────██████████───── ───███──────████████──────
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "dontshoot":
            ascii_art = """\
────────────────────────────────────██████────────────▐──────██▀██▀██──────▌───▐▐▐────█▄▄████▄▄█────▌▌▌─▐▐▐▐───▐█░■░██░■░█▌───▌▌▌▌▐███─▄▌▐█░░░██░░░█▌▐▄─███▌▐████▀─▐██████████▌─▀████▌▐███───▐██████████▌───███▌─███───▐████──████▌───███─────────████──████─────────────────████████───────────────────▀▀▀▀▀▀────────────────────────────────────
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "nice":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▄░█░▀█▀░█▀▀░█▀▀░█░░░░░░░░█░▀█░░█░░█░░░█▀▀░▀░░░░░░░░▀░░▀░▀▀▀░▀▀▀░▀▀▀░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "ggwp":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀▀▀░█▀▀▀░█▐▌█░█▀█░░░░░░░░█░▀█░█░▀█░█▐▌█░█▀▀░░░░░░░░▀▀▀▀░▀▀▀▀░░▀▀░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "banhammer":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░░░░░░░░██████▄░░░░░░▄▄▄░░░░░░░░░░░███▀▀▀▄▄▄▀▀▀░░░░░░░░░░░░░░░░▄▀▀▀▄░░░█▀▀▄░▄▀▀▄░█▄░█░░░░▄▄████░░█▀▀▄░█▄▄█░█▀▄█░░░░░██████░█▄▄▀░█░░█░█░▀█░░░░░░▀▀▀▀░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "afk":
            ascii_art = """\
░░█████╗░███████╗██╗░░██╗░░██╔══██╗██╔════╝██║░██╔╝░░███████║█████╗░░█████═╝░░░██╔══██║██╔══╝░░██╔═██╗░░░██║░░██║██║░░░░░██║░╚██╗░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "ace":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▀█░░█▀▀▀░█▀▀░░░░░░░░░░░░█▀▀▀█░█░░░   █▀▀░░░░░░░░░░░░▀░░░▀░▀▀▀▀░▀▀▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "urmom":
            ascii_art = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█▀█░░█▄░▄█░█▀█░█▄░▄█░░█░█░██▀░░█░▀░█░█░█░█░▀░█░░▀▀▀░▀░▀░░▀░░░▀░▀▀▀░▀░░░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "hmmm":
            ascii_art = """\
▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒▒▒▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒▒▒▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒▒▒▒█▀░░░░███░░░░▄█▄░░░░▀█▒▒▒▒█░░░░░░▀░░░░░▀█▀░░░░░█▒▒▒▒█░░░░░░░░░░░░░░░░░░░░█▒▒▒▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒▒▒▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒▒▒▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒▒▒▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒▒▒▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        elif text == "lol":
            ascii_art = """\
────────────────────────────────────██████───────────██──────█▀▀██▀▀█───██─────██─────██████████──██─────██────▐█■░░██░░░█▌─██─────██────▐█░░░██░░■█▌─██─────██────▐██████████▌─██─────██────▐██████████▌─██─────██────▐██▀████▀██▌─██─────█████──███▄▒▒▄███──█████──█████───███▒▒███───█████───────────▀▀▀▀▀▀────────────────────────────────────
"""
            # Create a button
            view = View()
            button = Button(label="Copy to clipboard", style=discord.ButtonStyle.primary, custom_id="copy_button")
            view.add_item(button)

            # Button callback
            async def button_callback(interaction: discord.Interaction):
                # Send the ASCII art back in a new message so the user can copy it
                await interaction.response.send_message(f"Here is your ASCII art:\n{ascii_art}")

            button.callback = button_callback

            # Send the ASCII art with the button
            await interaction.response.send_message(ascii_art, view=view)
        else:
            await interaction.response.send_message("Invalid choice!", ephemeral=True)

# Create a Cog to add the command
class Ascii(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.tree.add_command(AsciiGroup())  # Register the group command

async def setup(bot: commands.Bot):
    await bot.add_cog(Ascii(bot))
