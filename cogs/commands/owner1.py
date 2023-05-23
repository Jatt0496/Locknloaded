import discord
from discord.ext import commands


class devansh4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Owner commands"""
  
    def help_custom(self):
		      emoji = '<:icons_owner:1085776307343851574>'
		      label = "Owner"
		      description = "Shows You Developer Commands"
		      return emoji, label, description

    @commands.group()
    async def __Owner__(self, ctx: commands.Context):
        """`slist` , `restart` , `sync` , `np` , `np add` , `np remove` , `np list` , `bl show` , `bl add` , `bl remove` , `bdg` , `bdg add` , `bdg remove` , `dm` , `nick`"""