import discord
from discord.ext import commands
import json

class SHREEXD3110(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Autorole commands"""  

    def help_custom(self):
		      emoji = '<:riverse_autorole:1081587961717596241>'
		      label = "Autorole"
		      description = "Shows You Autorole Commands"
		      return emoji, label, description

    @commands.group()
    async def __Autorole__(self, ctx: commands.Context):
        """`autorole bots add` , `autorole bots remove` , `autorole bots` , `autorole config` , `autorole humans add` , `autorole humans remove` , `autorole humans` , `autorole reset all` , `autorole reset bots` , `autorole reset humans` , `autorole reset` , `autorole`"""