import discord
from discord.ext import commands


class itzherinvisible(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """ReactionRoles commands"""
  
    def help_custom(self):
		      emoji = '<:user:1081587321117352066>'
		      label = "ReactionRoles"
		      description = "Shows You ReactionRoles Commands"
		      return emoji, label, description

    @commands.group()
    async def __Reactionroles__(self, ctx: commands.Context):
        """`rr` , `reaction_add` , `reaction_remove` , `reactions`"""