import discord
from discord.ext import commands
import json

class devansh16(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ticket commands"""  

    def help_custom(self):
		      emoji = '<:ray_ticket:1072844286510501938>'
		      label = "Ticket"
		      description = "Shows You Ticket Commands"
		      return emoji, label, description

    @commands.group()
    async def __Tickets__(self, ctx: commands.Context):
        """`sendpanel`"""
       
    

    
   

