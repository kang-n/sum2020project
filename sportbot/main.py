import discord
import os
from sb_Football import on_fb

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!fb'):
        await on_fb(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)