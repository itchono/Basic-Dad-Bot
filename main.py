import discord
from discord.ext import commands
import random
import re
import os
import dotenv
from keep_alive import *

'''
BASIC DAD BOT

Developed for Skule 2T3 Server

By Mingde Yin (Itchono)

v1.0 June 6, 2020

Changelog:
1.0 - Initial Release
'''

DAD_CHANNELS = [709954286947270688, 718517287996620850, 718639004433514615]
# determines in which channels dadbot is allowed to operate

CHANCE = 0.25
# determines chance of activation

dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN')  # bot token; kept private

client = commands.Bot(command_prefix="dad ")

@client.command()
async def info(ctx : commands.Context):
    await ctx.send("I'm Dad Bot. I am currently have a {} percent chance of activating in channels where I am enabled.\nPing @itchono if anything goes wrong with me.")


@client.event
async def on_message(message : discord.Message):
    if message.channel.id in DAD_CHANNELS and message.author != client.user:
        
        arr = message.content.split(".")[0].split(" ") # take only the first sentence (user request)

        if random.random() <= CHANCE:
            try:
                for i in range(len(arr)):
                    if arr[i].translate(str.maketrans("", "", "#!$%&:\"\'()*+,-./;<=>?@[\\]^_`{|}~")).lower() == "im":
                        # detect if "I'm is in the string"
                        
                        await message.channel.send("Hi {}, I'm Dad!".format(" ".join(arr[i+1:])))
                        # sends the dreaded message
            except:
                pass

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("Hi, I'm Dad!"))
    # change status when bot is loaded
        
keep_alive() # start internal server to keep bot loaded
client.run(TOKEN) # log into Discord