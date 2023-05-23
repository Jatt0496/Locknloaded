import discord
from discord.ext import commands


class devanshshree3110(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Welcome commands"""
  
    def help_custom(self):
		      emoji = '<:ares_announce:1085775604948934676>'
		      label = "Welcomer"
		      description = "Shows You Welcome Commands"
		      return emoji, label, description

    @commands.group()
    async def __Welcomer__(self, ctx: commands.Context):
        """`greet` , `greet autodel` , `greet channel add` , `greet channel remove`, `greet channel` , `greet embed` , `greet image` , `greet message` , `greet ping` , `greet test` , `greet thumbnail` , `greet`"""