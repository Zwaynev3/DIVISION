import discord
from discord.ext import commands

class gen(commands.Cog):
	def __init__(self, bot):
		self.bot = bot	
	
	global accountypes
	accountypes = ['spotify', 'nordvpn', 'origin', 'minecraft', 'fortnite']
	
	
	global genfooter
	genfooter = "DivisionGen | discord.gg/yCn69Hz | Bot by Zwayne#1337"		
	
	global stockimport
	def stockimport(account):
		if account in accountypes:
			varname = f'{account}stock'		
			accountstock = [line.rstrip('\n') for line in open(f'stock/{account}.txt')]
			globals()[varname] = accountstock
			print("stock {} chargé : {}".format(account, len(accountstock)))
										
	@commands.Cog.listener()
	async def on_ready(self):
		for i in accountypes:
			stockimport(i)
		global genchan
		genchan = self.bot.get_channel(680137647347466325)
		
		
	@commands.command()
	async def testcog(self, ctx):
		await ctx.channel.send("Ca marche ptn")
		
		
	@commands.command(pass_context = True)
	async def spotify(self, ctx):
		if ctx.channel is genchan:
			account = spotifystock.pop(0)
			accountpv = discord.Embed(
			title = "Voici ton compte spotify.",
			description = account
			)
			accountpv.set_thumbnail(url=self.bot.user.avatar_url)
			await ctx.author.send(embed=accountpv)
			print("spotify generé")
			sendemb = discord.Embed(
			title = "Ton compte spotify t'as été envoyé en mp",
			description = ":white_check_mark:",
			color = 0
			)
			sendemb.set_footer(text=genfooter)
			sendemb.set_thumbnail(url=self.bot.user.avatar_url)
			await ctx.channel.send(embed=sendemb)
		else:
			await ctx.channel.send("Mauvais channel. " + genchan.mention)
		
	@commands.command(pass_context = True)
	async def nordvpn(self, ctx):
		if ctx.channel is genchan:
			account = nordvpnstock.pop(0)
			accountpv = discord.Embed(
			title = "Voici ton compte nordvpn.",
			description = account,
			color = 0
			)
			accountpv.set_thumbnail(url=self.bot.user.avatar_url)
			await ctx.author.send(embed=accountpv)
			print("nordvpn generé")
			sendemb = discord.Embed(
			title = "Ton compte nordvpn t'as été envoyé en mp",
			description = ":white_check_mark:",
			color = 0
			)
			sendemb.set_footer(text=genfooter)
			sendemb.set_thumbnail(url=self.bot.user.avatar_url)
			await ctx.channel.send(embed=sendemb)
		else:
			await ctx.channel.send("Mauvais channel. " + genchan.mention)

	@commands.command(pass_context = True)
	async def stock(self, ctx):
		if ctx.author.guild_permissions.administrator:
			stockemb = discord.Embed(
			title = "Voici le stock disponnible",
			color = 0
			)
			stockemb.add_field(name="Nordvpn", value =str(len(nordvpnstock)))
			stockemb.add_field(name="Spotify", value=str(len(spotifystock)))
			stockemb.add_field(name="Origin", value=str(len(originstock)))
			stockemb.add_field(name="Minecraft", value=str(len(minecraftstock)))
			stockemb.add_field(name="Fortnite", value=str(len(fortnitestock)))
			stockemb.set_footer(text="DivisionGen 1.0 | By Zwayne#1337")
			stockemb.set_thumbnail(url=self.bot.user.avatar_url)
			await ctx.channel.send(embed=stockemb)
		else:
			await ctx.channel.send("Tu as pas la permission.")
		
	@commands.command(pass_context = True)
	async def addstock(self, ctx, account: str = None, accountype: str = None):
		if not account:
			await ctx.channel.send("Met un compte")
		else:
			if not accountype:
				await ctx.channel.sebd("Precise le type du compte")
			else:
				if accountype in accountypes:
					if accountype == "spotify":
						file = open('stock/spotify.txt', 'a')
						file.write(f'\n{account}')
						spotifystock.append(account)
						await ctx.channel.send("Compte ajouté au stock spotify :white_check_mark:")
					elif accountype == "nordvpn":
						file = open('stock/nordvpn.txt', 'a')
						file.write(f'\n{account}')
						nordvpnstock.append(account)
						await ctx.channel.send("Compte ajouté au stock nordvpn :white_check_mark:")
					elif accountype == "origin":
						file = open('stock/origin.txt', 'a')
						file.write(f'\n{account}')
						originstock.append(account)
						await ctx.channel.send("Compte ajouté au stock origin :white_check_mark:")
					elif accountype == "fortnite":
						file = open('stock/fortnite.txt', 'a')
						file.write(f'\n{account}')
						fortnitestock.append(account)
						await ctx.channel.send("Compte ajouté au stock Fortnite :white_check_mark:")
					elif accountype == "minecraft":
						file = open('stock/minecraft.txt', 'a')
						file.write(f'\n{account}')
						minecraftstock.append(account)
						await ctx.channel.send("Compte ajouté au stock minecraft :white_check_mark:")
				else:
					await ctx.channel.send("{} n'est pas un type de compte existant dans le generateur".format(accountype))
	
	@commands.command(pass_context = True)
	async def origin(self, ctx):
		if ctx.channel is genchan:
			account = originstock.pop(0)
			accountpv = discord.Embed(
			title = "Voici ton compte origin.",
			description = account,
			color = 0
			)
			accountpv.set_thumbnail(url="https://image.noelshack.com/fichiers/2020/08/5/1582287272-5b447f12e99939b4572e32c0.png")
			await ctx.author.send(embed=accountpv)
			print("origin generé")
			sendemb = discord.Embed(
			title = "Ton compte origin t'as été envoyé en mp",
			description = ":white_check_mark:",
			color = 0
			)
			sendemb.set_footer(text=genfooter)
			sendemb.set_thumbnail(url="https://image.noelshack.com/fichiers/2020/08/5/1582287272-5b447f12e99939b4572e32c0.png")
			await ctx.channel.send(embed=sendemb)
		else:
			await ctx.channel.send("Mauvais channel. " + genchan.mention)				
		
		
	@commands.command(pass_context = True)
	async def mc(self, ctx):
		if ctx.channel is genchan:
			account = minecraftstock.pop(0)
			accountpv = discord.Embed(
			title = "Voici ton compte minecraft.",
			description = account,
			color = 0
			)
			accountpv.set_thumbnail(url="https://cdn.1min30.com/wp-content/uploads/2017/08/Minecraft-logos.jpg")
			await ctx.author.send(embed=accountpv)
			print("minecraft generé")
			sendemb = discord.Embed(
			title = "Ton compte minecraft t'as été envoyé en mp",
			description = ":white_check_mark:",
			color = 0
			)
			sendemb.set_footer(text=genfooter)
			sendemb.set_thumbnail(url="https://cdn.1min30.com/wp-content/uploads/2017/08/Minecraft-logos.jpg")
			await ctx.channel.send(embed=sendemb)
		else:
			await ctx.channel.send("Mauvais channel. " + genchan.mention)
	
	@commands.command(pass_context = True)
	async def fortnite(self, ctx):
		if ctx.channel is genchan:
			account = fortnitestock.pop(0)
			accountpv = discord.Embed(
			title = "Voici ton compte Fortnite:",
			description = account,
			color = 0
			)
			accountpv.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/fr/0/07/Fortnite_Battle_Royale_Logo.png")
			await ctx.author.send(embed=accountpv)
			print("fortnite generé")
			sendemb = discord.Embed(
			title = "Ton compte fortnite t'as été envoyé en mp",
			description = ":white_check_mark:",
			color = 0
			)
			sendemb.set_footer(text=genfooter)
			sendemb.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/fr/0/07/Fortnite_Battle_Royale_Logo.png")
			await ctx.channel.send(embed=sendemb)
		else:
			await ctx.channel.send("Mauvais channel. " + genchan.mention)
		
def setup(bot):
	bot.add_cog(gen(bot))