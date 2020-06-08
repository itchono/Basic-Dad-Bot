import discord
from discord.ext import commands
import random
import re
import os
import dotenv
from keep_alive import *
from utilities import *

'''
BASIC DAD BOT

Developed for Skule 2T3 Server

By Mingde Yin (Itchono)

v1.1 June 6, 2020

Changelog:
1.1 - Self ping upgrade, some extra commands
1.0 - Initial Release
'''

DAD_CHANNELS = [709954286947270688, 718517287996620850, 718639004433514615]
# determines in which channels dadbot is allowed to operate

CHANCE = 0.75
# determines chance of activation

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')  # bot token; kept private

client = commands.Bot(command_prefix="d!")

client.add_cog(SelfPing(client))

@client.command()
async def info(ctx : commands.Context):
    '''
    Basic bot info
    '''
    await ctx.send("I'm Dad Bot. I am currently have a {} percent chance of activating in channels where I am enabled.\nPing @itchono if anything goes wrong with me.".format(100*CHANCE))

@client.command()
async def supportme(ctx: commands.Context):
    '''
    Sends a motivating message
    '''
    await ctx.send("You make me proud, {}".format(ctx.author.mention))

@client.event
async def on_message(message : discord.Message):
    try:
        if message.channel.id in DAD_CHANNELS and message.author != client.user:
            
            arr = message.content.split(".")[0].split(" ") # take only the first sentence (user request)

            if random.random() <= CHANCE:
                try:
                    for i in range(len(arr)):
                        if arr[i].translate(str.maketrans("", "", "#!$%&:\"\'()*+,-./;<=>?@[\\]^_`{|}~")).lower() == "im":
                            # detect if "I'm is in the string"
                            
                            await message.channel.send("Hi {}, I'm Dad!".format(" ".join(arr[i+1:])))
                            # sends the dreaded message
                        return
                        # terminates the function
                except:
                    pass
    finally:
        await client.process_commands(message)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("[d!] Hi, I'm Dad!"))
    # change status when bot is loaded
        
keep_alive() # start internal server to keep bot loaded
client.run(TOKEN) # log into Discord