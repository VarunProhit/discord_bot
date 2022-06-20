# bot.py
import os
import json
import random
from urllib import response
import discord
import requests
# import urllib.request
from urllib.request import Request, urlopen
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
api_url ="https://type.fit/api/quotes"

@bot.command(name='quote')
async def getapi(ctx):
    try:
        response = requests.get(url = api_url)
    except Exception as e :
        print(str(e))
   
    print(response)
    # data = response.json()
    data = response.json()
    i = random.randint(0, 1643)
    auth = data[i]['author']
    text = data[i]['text']
    await ctx.send("```fix\n"+text+"\n:"+  auth+"```")


# @bot.event
# async def on_message(message):
#     if 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday! 🎈🎉')
@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        k = "created channel: "+channel_name
        await ctx.send(k)
    else:
        k = channel_name+ " Already exists"
        await ctx.send(k)




@bot.command(name='delete-channel')
@commands.has_role('admin')
async def delete_channel(ctx, channel_name):
    guild = ctx.guild    
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
   
   # if the channel exists
    if existing_channel is not None:
        await existing_channel.delete()
        await ctx.send(f'channel named, "{channel_name}", was deleted')
   # if the channel does not exist, inform the user
    else:
        await ctx.send(f'No channel named, "{channel_name}", was found')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
bot.run(TOKEN)


