import discord
from discord.ext import commands
import json

class devansh12(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ignore commands"""  

    def help_custom(self):
		      emoji = '<:i_channel:1072845262575390730>'
		      label = "Ignore"
		      description = "Shows You Ignore Commands"
		      return emoji, label, description

    @commands.group()
    async def __Ignore__(self, ctx: commands.Context):
        """`ignore` , `ignore channel add` , `ignore channel remove`"""
       