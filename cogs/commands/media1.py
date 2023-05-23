import discord
from discord.ext import commands


class anniemittal1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Media commands"""
  
    def help_custom(self):
		      emoji = '<:media:1084325986448965653>'
		      label = "Media"
		      description = "Show You Media Commands"
		      return emoji, label, description

    @commands.group()
    async def __Media__(self, ctx: commands.Context):
        """`media` , `media setup` , `media remove` , `config` , `media reset`"""