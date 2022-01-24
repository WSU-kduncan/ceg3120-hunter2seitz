import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]
    xavier_quotes = [
	'What doth life? Are we just fleshy blips in some meaningless stew of cosmic oblivion? Or is it vice-vers?' 
	'A dead child is like pudding the proof is in the fact that he probably looked like pudding when he got hit by that car'
	'Even the Bibles are ribbed, but whos pleasure?' 
	'Im a survivor, were a dying breed.' 

    ]

    if message.content == 'towel!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)
    if message.content == '!xavier':
	response = random.choice(xavier_quotes)
	await message.channel.send(response)

client.run(TOKEN)
