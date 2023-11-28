from typing import Any, Optional, Type
import discord
import os
import pathlib
import utils

from discord.ext import commands
from discord.ui import Select, View
from discord import SelectOption

PATH = pathlib.Path(__file__).parent.resolve()
GUILDS = utils.LoadJson(os.path.join(PATH, "..", "GUILDS.json"))

class SettingsDropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label='Panels', description='Add, edit, or delete panels', emoji='🪧'),
        ]

        super().__init__(placeholder='Choose setting..', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        view = View()
        view.add_item(self)
        await interaction.response.defer()
        await interaction.message.edit(content=f'{self.values[0]}',view=view)

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        print("cog ExampleCog loaded")
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with utils.JsonFileManager(os.path.join(PATH, "..", "GUILDS.json")) as guilds:
            guilds[str(guild.id)] = {}

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with utils.JsonFileManager(os.path.join(PATH, "..", "GUILDS.json")) as guilds:
            guilds.pop(str(guild.id), None)

    @commands.command()
    async def settings(self, ctx: commands.Context):
        if str(ctx.guild.id) in GUILDS:
            try:
                view = View()
                view.add_item(SettingsDropdown())
                await ctx.send("Please choose a setting from the dropdown below:", view=view)
            except BaseException as e:
                await ctx.send("**:octagonal_sign: Error: ** `{}`.".format(e))
        else:
            await ctx.send("**:octagonal_sign: Error: ** No guild initialized.")


async def setup(bot):
    await bot.add_cog(ExampleCog(bot))