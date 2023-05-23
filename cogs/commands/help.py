import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Ventura import Ventura
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
from utils import *
import json
from utils import help as vhelp
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

client = Ventura()


class HelpView(discord.ui.Select):
  def __init__(self):
    
    opts = [discord.SelectOption(label="Security", emoji="<:antinuke:1085777304107626526>", description="Shows You Security Commands"),
           discord.SelectOption(label="Moderation", emoji="<:moderation:1077510288796045332>", description="Shows You Moderation Commands"),
           discord.SelectOption(label="Welcome", emoji="<:icons_join:1089768448776753263>", description="Shows You Welcome Commands"),
           discord.SelectOption(label="Logging", emoji="<:artic_logging:1072845568059113472>", description="Shows You Logging Commands"),        
           discord.SelectOption(label="Utility", emoji="<:i_guardian:1085783897998114876>", description="Shows You Utility Commands"), 
           discord.SelectOption(label="Games", emoji="<:Games:1072838559456833536>", description="Shows You Games Commands"), 
           discord.SelectOption(label="Server", emoji="<:rnt_icons_serverpartner:1089613997298434118>", description="Shows You Server Commands"), 
           discord.SelectOption(label="Vanityroles", emoji="<:icons_premiumchannel:1090596344609124363>", description="Shows You Vanityroles Commands"),
           
           

            
            
           ]
    super().__init__(placeholder="Select a Category of Main Modules", max_values=1, min_values=1, options=opts)



  
  async def callback(self, interaction: discord.Interaction):

      mod = interaction.client.get_cog("anti")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Security":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Moderation")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Moderation":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Welcomer")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Welcome":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Logging")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Logging":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Utility")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Utility":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Games")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Games":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Server")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Server":
        await interaction.response.edit_message(embed=embed_mod)


      mod = interaction.client.get_cog("Vanity")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Vanityroles":
        await interaction.response.edit_message(embed=embed_mod)
        
      

      

      













class dropdown(discord.ui.View):
  def __init__(self, *, timeout=None):
     super().__init__(timeout=timeout)
     self.add_item(HelpView())
     self.response = None












class HelpVi(discord.ui.Select):
  def __init__(self):
    
    opts = [discord.SelectOption(label="Raidmode", emoji="<:ares_kick:1089766124352188496>", description="Shows You Raidmode Commands"),
           discord.SelectOption(label="Verification", emoji="<:ares_verified:1084121458407641189>", description="Shows You Verification Commands"),
           discord.SelectOption(label="Voice", emoji="<:voice:1085786179699494955>", description="Shows You Voice Commands"), 
           discord.SelectOption(label="Autoresponse", emoji="<:ET_autoedit:1090542313186545724>", description="Shows You Autoresponse Commands"),                  discord.SelectOption(label="Ignore", emoji="<:i_channel:1072845262575390730>", description="Shows You Ignore Commands"), 
           discord.SelectOption(label="General", emoji="<:i_globe:1085777373552717885>", description="Shows You General Commands"), 
           discord.SelectOption(label="Owner", emoji="<:icons_owner:1085776307343851574>", description="Shows You Owner Commands"),
                     
           ]
    super().__init__(placeholder="Select a Category of Advanced Modules", max_values=1, min_values=1, options=opts)


  
  async def callback(self, interaction: discord.Interaction):

      mod = interaction.client.get_cog("Raidmode")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Raidmode":
        await interaction.response.edit_message(embed=embed_mod)

    
      mod = interaction.client.get_cog("Verification")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Verification":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Voice")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Voice":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Autoresponder")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Autoresponse":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Ignore")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Ignore":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("General")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "General":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Owner")
      embed_mod = discord.Embed(title=f"**__{mod.qualified_name}__**".title(), description=mod.description, color=0x50101)
      popcorn = ' **,** '.join([f"`{cmd.qualified_name}`" for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.set_footer(text="Thanks For Choosing Ventura!")
      embed_mod.add_field(name="", value=popcorn, inline=False)
      if self.values[0] == "Owner":
        await interaction.response.edit_message(embed=embed_mod)


      







        
class drop(discord.ui.View):
  def __init__(self, *, timeout=None):
     super().__init__(timeout=timeout)
     self.add_item(HelpVi())
     self.response = None


class HelpCommand(commands.HelpCommand):

    async def on_help_command_error(self, ctx, error):
        damn = [
            commands.CommandOnCooldown, commands.CommandNotFound,
            discord.HTTPException, commands.CommandInvokeError
        ]
        if not type(error) in damn:
            await self.context.reply(
                f"Unknown Error Occurred\n{error.original}",
                mention_author=False)
        else:
            if type(error) == commands.CommandOnCooldown:
                return

                return await super().on_help_command_error(ctx, error)

    async def command_not_found(self, string: str) -> None:
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:astroz_cross:1072464778313879634> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/z7B4MXCZ9K)",
                color=0x50101)
            await self.context.reply(embed=embed, mention_author=False)
        else:

            if string in ("security", "anti","antinuke"):
                cog = self.context.bot.get_cog("Antinuke")
                with suppress(discord.HTTPException):
                    await self.send_cog_help(cog)
            else:
                msg = f"Command `{string}` is not found...\n"
                devansh = await self.context.bot.fetch_user(810352682823843861)
                cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
                mtchs = get_close_matches(string, cmds)
                if mtchs:
                    for okaay, okay in enumerate(mtchs, start=1):
                        msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
                embed1 = discord.Embed(
                    color=0x50101,
                    title=f"Command `{string}` is not found...\n",
                    description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
                embed1.set_footer(text=f"Developed By {devansh}",
                                  icon_url=devansh.display_avatar.url)
                return None

    async def send_bot_help(self, mapping):
        await self.context.typing()
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            bled = json.load(f)
        if str(self.context.author.id) in bled["ids"]:
            embed = discord.Embed(
                title="<a:astroz_cross:1072464778313879634> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/z7B4MXCZ9K)",
                color=0x50101)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]
        perms = discord.Permissions.none()
        perms.read_messages = True
        perms.external_emojis = True
        perms.send_messages = True
        perms.manage_roles = True
        perms.manage_channels = True
        perms.ban_members = True
        perms.kick_members = True
        perms.manage_messages = True
        perms.embed_links = True
        perms.read_message_history = True
        perms.attach_files = True
        perms.add_reactions = True
        perms.administrator = True
        inv = discord.utils.oauth_url(self.context.bot.user.id,
                                      permissions=perms)
        filtered = await self.filter_commands(self.context.bot.walk_commands(),
                                              sort=True)
        devansh = await self.context.bot.fetch_user(810352682823843861)
        embed = discord.Embed(
            title="Help Command Overview :",
            description=
            f"<a:dots:1047124596396130375> Prefix for this server is `'-'`\n<a:dots:1047124596396130375> Total Commands: {len(set(self.context.bot.walk_commands()))} | Usable by you (here): {len(set(filtered))}\n<a:dots:1047124596396130375> Type `'-'help <command | module>` for more info.\n<a:dots:1047124596396130375> [Invite]({inv}) | [Support](https://discord.gg/lnl) |",
            color=0x2f3136)
        embed.set_thumbnail(url=self.context.bot.user.display_avatar.url)

        embed.set_footer(text=f"Developed By {devansh}",
                         icon_url=devansh.display_avatar.url)
        embed.add_field(
            name="__Main Modules__",
            value=
            """<:antinuke:1085777304107626526> Security\n<:moderation:1077510288796045332> Moderation\n<:icons_join:1089768448776753263> Welcome\n<:artic_logging:1072845568059113472> Logging\n<:i_guardian:1085783897998114876> Utility\n<:Games:1072838559456833536> Games\n<:rnt_icons_serverpartner:1089613997298434118> Server\n<:icons_premiumchannel:1090596344609124363> Vanityroles""",
            inline=True)
        embed.add_field(
            name="__Advance Modules__",
            value=
            """<:ares_kick:1089766124352188496> Raidmode\n<:ares_verified:1084121458407641189> Verification\n<:voice:1085786179699494955> Voice\n<:ET_autoedit:1090542313186545724> Autoresponse\n<:i_channel:1072845262575390730> Ignore\n<:i_globe:1085777373552717885> General\n<:icons_owner:1085776307343851574> Owner""",
            inline=True)
        embed.add_field(
            name="__Extra Modules__",
            value=
            """<:riverse_autorole:1081587961717596241> Autorole\n<:ray_ticket:1072844286510501938> Ticket\n<:ET_raid:1090592185533075457> Vcrole\n<:icons_channelfollowed:1090592608360857690> Note\n<:icons_monitor:1085779063806902354> Media\n<:icons_repeat:1073269071002488942> Encryption\n<:emoji_7:1090594435949133874> Music\n<:nsfw:1077509046011187274> Nsfw""",
            inline=True)
        embed.set_author(name=self.context.author.name,
                         icon_url=self.context.author.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()
        
      

        view = vhelp.View(mapping=mapping,
                          ctx=self.context,
                          homeembed=embed,
                          ui=2).add_item(HelpView()).add_item(HelpVi())
        await self.context.reply(embed=embed, mention_author=False, view=view)

    async def send_command_help(self, command):
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:astroz_cross:1072464778313879634> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/z7B4MXCZ9K)",
                color=0x50101)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
            embed = discord.Embed(
                description=
                f"""```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""",
                color=0x50101)
            alias = ' | '.join(command.aliases)

            embed.add_field(
                name="**Aliases**",
                value=f"{alias}" if command.aliases else "No Aliases",
                inline=False)
            embed.add_field(
                name="**Usage**",
                value=f"`{self.context.prefix}{command.signature}`\n")
            embed.set_author(name=f"{command.cog.qualified_name.title()}",
                             icon_url=self.context.bot.user.display_avatar.url)
            await self.context.reply(embed=embed, mention_author=False)

    def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

    def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'


    async def send_group_help(self, group):
        with open('blacklist.json', 'r') as f:
            idk = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in idk["ids"]:
            embed = discord.Embed(
                title="<a:astroz_cross:1072464778313879634> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/z7B4MXCZ9K)",
                color=0x50101)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in group.commands]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{group.qualified_name} Commands",
            description="<...> Duty | [...] Optional\n\n",
            color=0x50101,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()

        
    
    async def send_cog_help(self, cog):
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:astroz_cross:1072464778313879634> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/z7B4MXCZ9K)",
                color=0x50101)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        #await self.context.typing()
        entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in cog.get_commands()]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{cog.qualified_name.title()} ({len(cog.get_commands())})",
            description="<...> Duty | [...] Optional\n\n",
            color=0x50101,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()


class Help(Cog, name="help"):

    def __init__(self, client: Ventura):
        self._original_help_command = client.help_command
        attributes = {
            'name':
            "help",
            'aliases': ['h'],
            'cooldown':
            commands.CooldownMapping.from_cooldown(1, 5,
                                                   commands.BucketType.user),
            'help':
            'Shows help about bot, a command or a category'
        }
        client.help_command = HelpCommand(command_attrs=attributes)
        client.help_command.cog = self

    async def cog_unload(self):
        self.help_command = self._original_help_command
    def help_custom(self):
		      emoji = '<:DH_Home:1078225277324370020>'
		      label = "Help"
		      description = "Shows You Help Menu"
		      return emoji, label, description


  