import os
import sys
import discord 
import traceback 
import jishaku #importing jishaku , it is a nice module which helps debugging and cog loading and unloading module so you dont have to make a load and unload stuff
from discord.ext import commands #importing the commands and task frame work 



prefix = '+' #assigning the bot prefix 
intents = discord.Intents.all() #loading all intents 
bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True, intents=intents)#AutoSharded makes your bot a bit faster just a bit may help in latency
bot.remove_command('help') #removing the deafult help command 
bot.DEFAULT_PREFIX = prefix
bot.color = 0x2F3136 #assigning the bot color , not nessecary .



@bot.event #making a event here for on ready
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('discord.py')) # making the bot status
    print("Bot is running.")


extensions = [
			  'cogs.mod',
			  'cogs.fun',           #importing our cogs 
			  'cogs.apiinfo',
			  'cogs.info',
			  'cogs.extrafun',
			  'cogs.ping',
			  'cogs.animemanga',
			  'cogs.help',
			  'cogs.imagemaniplulation'
]
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Error loading the {extension}", file=sys.stderr)
            traceback.print_exc()
            
 bot.load_extension("jishaku")#loading the jishaku module 
 
bot.run("token")# your token here should be in string format or just within inverted commas
