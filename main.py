# bot.py
import os

import discord
from dotenv import load_dotenv
from message_handlers.memes import send_random_meme
from message_handlers.utility import check_valid_url

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # If bot has messaged in the group
    if message.author == client.user:
        return

    msg = message.content.lower()
    

    # this bot should only respond to messages with ayaya
    if  "ayaya" in msg:
        if "meme" in msg:
            url = send_random_meme()
            if check_valid_url(url):
                await message.channel.send(url)
            else:
                await message.channel.send("No AYAYA Found :(")
        else:
            url = send_random_meme("AYAYA")
            if check_valid_url(url):
                await message.channel.send(url)
            else:
                await message.channel.send("AYAYAYA AYAYAYA AYAYAYA AYAYAYA")
        

client.run(TOKEN)
