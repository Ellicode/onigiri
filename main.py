import asyncio
import os
import pathlib
from dotenv import load_dotenv
from discord.ext import commands
import discord
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PATH = pathlib.Path(__file__).parent.resolve()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load extensions
extensions = [
    'cogs.example_cog',
]

async def load_extensions():
    for extension in extensions:
        await bot.load_extension(extension)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(load_extensions())
    bot.run(TOKEN)