import discord
from discord.ext import commands
from discord import Activity, ActivityType
import configuration
import random
import pyPrivnote

client = commands.Bot(command_prefix = "d!")



client.remove_command('help')

helptype = 0

		
@client.event
async def on_ready():
	print("Demarrage du bot...")
	print('Connecté en tant que '+client.user.name+' (ID:'+str(client.user.id)+') | Actuellement connecté à '+str(len(client.guilds))+' serveurs et '+str(len(set(client.get_all_members())))+' utilisateurs.')
	print("DivisionGen v1.0 | By Zwayne#1337")
	
	#presence
	await client.change_presence(status=discord.Status.idle, activity=Activity(name=f'{len(set(client.get_all_members()))} membres sur {len(client.guilds)} serveurs', type=ActivityType.watching))			


#load les cogs
		
coglist = ['gen','dmall','help','mod','fun']				
for i in coglist:
	client.load_extension(f'modules.{i}')
	print(f'extension chargé : {i}')														
																																				
			
client.run(configuration.TOKEN)