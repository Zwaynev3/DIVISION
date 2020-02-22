import discord
from discord.ext import commands

class mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		global muterole
		muterole = None
		
		
		global noperm
		async def noperm(ctx):
			await ctx.channel.send("Tu n'as pas les permissions.")
			
		global nomember
		async def nomember(ctx):
			await ctx.channel.send("Mentionne un membre.")
		
		
		global footer
		footer = "DivisionBot | https://discord.gg/yCn69Hz | By Zwayne#1337"
		
	@commands.command()
	async def ban(self, ctx, member: discord.Member = None, *, content:str = None):
		if ctx.author.guild_permissions.ban_members:
			if not member:
				await nomember(ctx)
			else:
				banemb = discord.Embed(
				title = "Tu as été banni du serveur {} par {} pour la raison suivante :".format(ctx.guild.name, ctx.author.name), description = "Raison du bannissement : {}".format(content), color = 0)
				await member.send(embed=banemb)
				try:														
					await member.ban()
				except:
					await ctx.channel.send("Impossible de bannir cet utilisateur.")
					return
				await ctx.channel.send("{} a été banni".format(member.name))					
		else:			
			await noperm(ctx)
			
	@commands.command()
	async def kick(self, ctx, member: discord.Member = None, *, content:str = None):
		if ctx.author.guild_permissions.kick_members:
			if not member:
				await nomember(ctx)
			else:
				banemb = discord.Embed(
				title = "Tu as été kick du serveur {} par {} pour la raison suivante :".format(ctx.guild.name, ctx.author.name), description = "Raison du kick : {}".format(content), color = 0)
				await member.send(embed=banemb)
				try:														
					await member.kick()
				except:
					await ctx.channel.send("Impossible de kick cet utilisateur.")
					return
				await ctx.channel.send("{} a été kick".format(member.name))					
		else:			
			await noperm(ctx)
			
	@commands.command()
	async def setmuterole(self, ctx, role: discord.Role = None):
		if ctx.author.guild_permissions.administrator:
			if not role:
				await ctx.channel.send("Mentionne un role.")
			else:
				global muterole
				muterole = role
				await ctx.channel.send(":white_check_mark:")
		else:
			await noperm(ctx)
			
	@commands.command()
	async def mute(self, ctx, member: discord.Member = None):
		if ctx.author.guild_permissions.kick_members:
			if not member:
				await nomember(ctx)
			else:
				if not muterole:
					await ctx.channel.send("Il faut d'abord configurer le role mute.")
				else:
					
					await ctx.channel.send(member.mention + " a été mute")
					await member.add_roles(muterole)								
		else:
			await noperm(ctx)
	
	
	@commands.command()
	async def unmute(self, ctx, member: discord.Member = None):
		if ctx.author.guild_permissions.administrator:
			if not member:
				nomember(ctx)
			else:
				if not muterole:
					return				
				elif muterole in member.roles:
					await member.remove_roles(muterole)
					await ctx.channel.send(member.mention + " a été unmute.")
				else:
					await ctx.channel.send("Ce membre n'est pas mute.")			
		else:
			noperm(ctx)
			
		
		
			
def setup(bot):
	bot.add_cog(mod(bot))