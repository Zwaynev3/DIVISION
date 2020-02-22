import discord
from discord.ext import commands
import time
from time import sleep

class dmall(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context = True)
	async def dmall(self, ctx, *, content: str):
		if ctx.author.guild_permissions.administrator:	
			await ctx.channel.send('Demarrage, {} membres vont etre mp...'.format(len(set(self.bot.get_all_members()))))
			allmembers = self.bot.get_all_members()
			for member in allmembers:
				try:										
					await member.send(content=content)
					await ctx.channel.send("MP envoyé à : {} :white_check_mark:  ".format(member))
					time.sleep(1.1)
				except:
					print("erreur de dm")
					await ctx.channel.send("Erreur, mp non envoyé à : {} :x: ".format(member))
					time.sleep(1.1)
			await ctx.channel.send("Terminé :white_check_mark:, {} membres on été mp".format(len(set(self.bot.get_all_members()))))
		else:
			await ctx.channel.send("Tu n'as pas la permission.")

	@commands.command(pass_context = True)
	async def dmlocal(self, ctx, *, content: str):
		if ctx.author.guild_permissions.administrator:
			
			await ctx.channel.send('Demarrage, {} membres vont etre mp...'.format(len(ctx.guild.members)))
			for member in ctx.guild.members:
				try:
					await member.send(content=content)
					await ctx.channel.send("MP envoyé à : {} :white_check_mark:  ".format(member))
					time.sleep(1.1)
				except:
						print("erreur de dm")
						await ctx.channel.send("Erreur, mp non envoyé à : {} :x: ".format(member))
						time.sleep(1.1)
			await ctx.channel.send("Terminé :white_check_mark:")
			await ctx.channel.send('Dmlocal terminé sur le serveur {} avec {} membres.'.format(ctx.guild.name, len(ctx.guild.members)))
				
		else:
			await ctx.channel.send("Tu n'as pas la permission")

	@commands.command(pass_context = True)
	async def serverlist(self, ctx):
		if ctx.author.guild_permissions.administrator:
			allmembers = self.bot.get_all_members()
			await ctx.channel.send("{} membres disponnibles sur {} serveurs.".format(len(set(allmembers)), len(self.bot.guilds)))
			serverlistt = discord.Embed(
			title = "Liste des serveurs",
			description = "Liste de tous les serveurs du bot"
			)
			serverlistt.set_footer(text="ZwayneDM | by Zwayne#1337")
			serverlistt.set_thumbnail(url=self.bot.user.avatar_url)
			for guild in self.bot.guilds:
				serverlistt.add_field(name="{} | ID : {}".format(guild.name, guild.id), value= "{} membres".format(len(guild.members)))
				
			await ctx.channel.send(embed=serverlistt)
			print("Liste des serveurs affichés.")
		else:
			await ctx.channel.send("Pas les permissions.")	

	@commands.command(pass_context = True)
	async def dmserver(self, ctx, idd: int, *, content):
		if ctx.author.guild_permissions.administrator:
			dmguild = self.bot.get_guild(idd)
			if not dmguild:
				ctx.channel.send("Erreur, serveur introuvable.")
			else:
				await ctx.channel.send("Demarrage sur le serveur {}, {} membres vont etre mp..".format(dmguild.name, len(dmguild.members)))
				for member in dmguild.members:
					try:
						await member.send(content=content)
						await ctx.channel.send("MP envoyé à : {} :white_check_mark:  ".format(member))
						time.sleep(1.1)
					except:
						print("erreur de dm")
						await ctx.channel.send("Erreur, mp non envoyé à : {} :x: ".format(member))
						time.sleep(1.1)
				await ctx.channel.send("Terminé :white_check_mark:")
				print('Dmserver terminé sur le serveur {} avec {} membres.'.format(dmguild.name, len(dmguild.members)))
				await ctx.channel.send('Dmserver terminé sur le serveur {} avec {} membres.'.format(dmguild.name, len(dmguild.members)))
		else:
			ctx.channel.send("Tu n'as pas les permissions.")
                			
	@commands.command(pass_context = True)
	async def sd(self, ctx):
		if ctx.author.guild_permissions.administrator:
			await ctx.channel.send("Le bot va s'eteindre..")
			await self.bot.close()
		else:
			await ctx.channel.send("impossible avec tes permissions")
		

	@commands.command(pass_context = True)
	async def serverinfo(self, ctx, idd: int):
		if ctx.author.guild_permissions.administrator:
			server = self.bot.get_guild(idd)
			if not server:
				await ctx.channel.send("Serveur introuvable")
			else:
				srvinfo = discord.Embed(
				title = "Information serveur : {}".format(server.name),
				description = "ID : {}".format(server.id),
				color = 0
				)
				srvinfo.set_footer(text="ZwayneDM | by Zwayne#1337")
				srvinfo.set_thumbnail(url=server.icon_url)
				srvinfo.add_field(name="Nom du serveur", value=server.name)
				srvinfo.add_field(name="Nombre de membres", value="{}".format(len(server.members)))
				srvinfo.add_field(name="ID du serveur", value=str(server.id))
				await ctx.channel.send(embed=srvinfo)
			
		else:
			await ctx.channel.send("Tu n'as pas la permission.")
		
def setup(bot):
	bot.add_cog(dmall(bot))
		