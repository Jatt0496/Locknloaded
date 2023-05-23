import discord
from discord.ext import commands


class anniemittal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Verification commands"""
  
    def help_custom(self):
		      emoji = '<:ares_verified:1084121458407641189>'
		      label = "Verification"
		      description = "Show You Verification Commands"
		      return emoji, label, description

    @commands.group()
    async def __Verification__(self, ctx: commands.Context):
        """`verification` , `verification enable` , `verification disable` , `verification config`"""