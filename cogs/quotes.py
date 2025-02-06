import discord
from discord.app_commands import commands
import random
import asyncio
from discord import app_commands
from discord.ext import commands


class Quotes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="quotes", description="gives a famous quote")
    async def quotes(self, interaction: discord.Interaction):
        quotes = [
            ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
            ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
            ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
            ("Success is not final, failure is not fatal: It is the courage to continue that counts.",
             "Winston Churchill"),
            ("Happiness depends upon ourselves.", "Aristotle"),
            ("It is not length of life, but depth of life.", "Ralph Waldo Emerson"),
            ("To love oneself is the beginning of a lifelong romance.", "Oscar Wilde"),
            ("Life is really simple, but we insist on making it complicated.", "Confucius"),
            ("An unexamined life is not worth living.", "Socrates"),
            ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
            ("The best way to predict the future is to create it.", "Peter Drucker"),
            ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
            ("You must be the change you wish to see in the world.", "Mahatma Gandhi"),
            ("Nothing is impossible, the word itself says 'I'm possible'!", "Audrey Hepburn"),
            ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
            ("Act as if what you do makes a difference. It does.", "William James"),
            ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison"),
            ("If you cannot do great things, do small things in a great way.", "Napoleon Hill"),
            ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
            ("Doubt kills more dreams than failure ever will.", "Suzy Kassem"),
            ("Quality is not an act, it is a habit.", "Aristotle"),
            ("A goal without a plan is just a wish.", "Antoine de Saint-Exupéry"),
            ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs"),
            ("I would rather die of passion than of boredom.", "Vincent van Gogh"),
            ("Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.",
             "Buddha"),
            ("You only live once, but if you do it right, once is enough.", "Mae West"),
            ("Keep your face always toward the sunshine—and shadows will fall behind you.", "Walt Whitman"),
            ("The journey of a thousand miles begins with one step.", "Lao Tzu"),
            ("Turn your wounds into wisdom.", "Oprah Winfrey"),
            ("If opportunity doesn't knock, build a door.", "Milton Berle"),
            ("What lies behind us and what lies before us are tiny matters compared to what lies within us.",
             "Ralph Waldo Emerson"),
            ("Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless.",
             "Jamie Paolinetti"),
            ("Strive not to be a success, but rather to be of value.", "Albert Einstein"),
            ("It always seems impossible until it’s done.", "Nelson Mandela"),
            ("We may encounter many defeats but we must not be defeated.", "Maya Angelou"),
            ("Knowing yourself is the beginning of all wisdom.", "Aristotle"),
            ("Everything you’ve ever wanted is on the other side of fear.", "George Addair"),
            ("If you want to lift yourself up, lift up someone else.", "Booker T. Washington"),
            ("No act of kindness, no matter how small, is ever wasted.", "Aesop"),
            ("Courage is resistance to fear, mastery of fear—not absence of fear.", "Mark Twain"),
            ("You can't use up creativity. The more you use, the more you have.", "Maya Angelou"),
            ("It is never too late to be what you might have been.", "George Eliot"),
            ("Everything has beauty, but not everyone sees it.", "Confucius"),
            ("Injustice anywhere is a threat to justice everywhere.", "Martin Luther King Jr."),
            ("Failure is another stepping stone to greatness.", "Oprah Winfrey"),
            ("The secret of getting ahead is getting started.", "Mark Twain"),
            ("Try to be a rainbow in someone’s cloud.", "Maya Angelou"),
            ("Do what you feel in your heart to be right – for you’ll be criticized anyway.", "Eleanor Roosevelt"),
            ("He who opens a school door, closes a prison.", "Victor Hugo"),
            ("Don’t wait. The time will never be just right.", "Napoleon Hill"),
        ]

        quote = random.choice(quotes)
        await interaction.response.send_message(quote)

async def setup(bot: commands.Bot):
    """Adds the Updater cog to the bot."""
    await bot.add_cog(Quotes(bot))
