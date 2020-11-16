# bot.py
import os

import discord
from message_handlers.memes import send_random_meme
from message_handlers.utility import check_valid_url
from message_handlers.rasa_chat import get_chat_message

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
            entities = msg.split()
            msg = ""
            if entities >= 3:
                msg = entities[2]
            url = send_random_meme(msg)
            if check_valid_url(url):
                await message.channel.send(url)
            else:
                await message.channel.send("No AYAYA Found :(")
        else:
            msg_list = msg.split()
            msg_list.remove("ayaya")
            response = get_chat_message(" ".join(msg_list))
            await message.channel.send(response)


client.run(TOKEN)
