import discord
import os

from dotenv import load_dotenv
from sb_Football import on_fb, setPlayer, getStats

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

sport = ''
player = ''
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('!fb'):
        if message.content.startswith('!fb.stats'):
            getStats(player)
        await on_fb(message)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    print(str(reaction.emoji))
    global player
    react,player = setPlayer(str(reaction.emoji))
    player = ''.join(player)
    #print(player)
    await channel.send(react)
    #await channel.send('{} is the emoji just inputted'.format(reaction.emoji))
    


client.run(TOKEN)