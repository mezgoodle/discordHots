import discord
from dotenv import load_dotenv
import requests

load_dotenv()
import os
import json
import random
import datetime
from replit import db
from keepAlive import keep_alive


client = discord.Client()


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    if 'encouragments' in db.keys():
        encouragments = db['encouragments']
        encouragments.append(encouraging_message)
        db['encouragments'] = encouragments
    else:
        db['encouragments'] = [encouraging_message]

def delete_encouragement(index):
    encouragments = db['encouragments']
    if len(encouragments) > index:
        del encouragments[index]
        db['encouragments'] = encouragments


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

keep_alive()
client.run(os.getenv('TOKEN'))
