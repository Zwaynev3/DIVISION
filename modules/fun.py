import discord
from discord.ext import commands
import pyPrivnote


class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
		
	@commands.command(pass_context=True)
	async def privnote(self, ctx, *,content:str = None):
		if not content:
			await ctx.channel.send("Pas de texte")
		else:
			await ctx.message.delete()
			await ctx.channel.send(pyPrivnote.create_note(content))
		
def setup(bot):
	bot.add_cog(fun(bot))