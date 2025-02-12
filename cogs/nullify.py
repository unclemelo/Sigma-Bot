import discord
from discord.ext import commands
from functools import wraps

## Developer IDs ##
devs = {1268070879598870601, 1331452332688543815}  ## Replace with all the discord ids of bot Admins
###################

def is_dev():
    """Decorator to restrict commands to developers."""

    def predicate(func):
        @wraps(func)
        async def wrapper(self, interaction: discord.Interaction, *args, **kwargs):
            if interaction.user.id in self.devs:
                return await func(self, interaction, *args, **kwargs)
            await interaction.response.send_message(
                "This command is restricted to certain people.", ephemeral=True
            )

        return wrapper

    return predicate

class NullifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nullify')
    @commands.has_permissions(manage_channels=True, manage_roles=True)
    @is_dev()
    async def nullify(self, ctx):
        guild = ctx.guild
        
        # Rename all channels to "null"
        for channel in guild.channels:
            try:
                await channel.edit(name="null")
            except discord.errors.Forbidden:
                await ctx.send(f"Couldn't rename channel {channel.name}")
        
        # Rename all roles to "null"
        for role in guild.roles:
            if role.name != "@everyone":  # Cannot rename @everyone role
                try:
                    await role.edit(name="null")
                except discord.errors.Forbidden:
                    await ctx.send(f"Couldn't rename role {role.name}")

        await ctx.send("All channels and roles have been renamed to 'null' where possible.")

def setup(bot):
    bot.add_cog(NullifyCog(bot))