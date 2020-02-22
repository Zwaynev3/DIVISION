import discord
from discord.ext import commands

class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(pass_context=True)
	async def help(self, ctx, helptype: str = None):
		if not helptype:
			
			ehelp= discord.Embed(
			title = "Liste des catégories de commandes",
			color = 0
			)
			ehelp.set_footer(text="DivisionBot | by Zwayne#1337")
			ehelp.set_thumbnail(url=self.bot.user.avatar_url)
			ehelp.add_field(name="Commandes dmall (administrateur)", value="d!help dmall")
			ehelp.add_field(name="Commandes generateur", value ="d!help gen")
			ehelp.add_field(name="Commandes de modération", value = "d!help mod")
			ehelp.add_field(name="Commandes d'administration/configuration", value="d!help admin")
		elif helptype == "dmall":
			ehelp = discord.Embed(
			title = "Liste des commandes dmall",
			description = "Reservé aux administrateurs",
			color = 0
			)
			
			ehelp.add_field(name="serverlist", value="Affiche la liste des serveurs du bot, leur id et leur nombre de membre.")
			ehelp.set_footer(text="ZwayneDM | by Zwayne#1337")
			ehelp.add_field(name="dmall [message] ", value="Permet d'envoyer un message a tous les membres accessibles par le bot (tous serveurs). " )
			ehelp.add_field(name="dmlocal [message]", value="Permet d'envoyer un message uniquement aux membres du serveur ou la commande est executée. ")
			ehelp.add_field(name="dmserver (ID du serveur) [message]", value="Permet d'envoyer un message a tous les membres du serveur voulu, si le bot est dessus")
			ehelp.set_thumbnail(url=self.bot.user.avatar_url)
		elif helptype == "gen":
			
			ehelp = discord.Embed(
		title ="Aide sur les commandes du generateur",
		color = 0
		)
			ehelp.set_footer(text="DIVISION DM | by Zwayne#1337")
			ehelp.set_thumbnail(url=self.bot.user.avatar_url)
			ehelp.add_field(name="d!spotify", value="Vous envoie un compte spotify en message privé")
			ehelp.add_field(name="d!nordvpn", value="Vous envoie un nordvpn en message privé")
			ehelp.add_field(name="d!origin", value="Vous envoie un compte origin en message privé")
			ehelp.add_field(name="d!stock", value="Affiche le stock.")
			ehelp.add_field(name="d!addstock (compte) [type de compte]", value="Ajoute un compte au stock du bot, reservé aux fournisseurs")
			
		elif helptype == "mod":
			ehelp = discord.Embed(
		title ="Aide sur les commandes du generateur",
		color = 0
		)
			ehelp.set_footer(text="DivisionBot | by Zwayne#1337")
			ehelp.set_thumbnail(url=self.bot.user.avatar_url)
			ehelp.add_field(name="d!ban (membre) [raison]",value="Ban le membre mentionné")
			ehelp.add_field(name="d!kick (membre) [raison]",value="kick le membre mentionné")
			ehelp.add_field(name="d!mute (membre)", value="Mute le membre mentionné")
			ehelp.add_field(name="d!unmute (membre)", value="Unmute le membre mentionné")
			ehelp.add_field(name="d!softban (membre)", value="ban et deban instantanement pour supprimer les message d'un utilisateur")
			ehelp.add_field(name="d!purge (nombre de message a purger)", value="Purge les messages")
		elif helptype == "admin":
			return
		elif helptype == "fun":
			return
			
		else:
			await ctx.channel.send("La page d'aide {} n'existe pas.".format(helptype))
			
	
		await ctx.channel.send(embed=ehelp)
		
		
		
def setup(bot):
	bot.add_cog(help(bot))