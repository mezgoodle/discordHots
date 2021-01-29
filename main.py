import discord
from dotenv import load_dotenv
import requests

load_dotenv()
import os
import json
import random
from replit import db


client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def update_encouragements(encouraging_message):
    if 'encouragments' in db.key():
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

    options = starter_encouragements
    if 'encouragments' in db.keys():
        options += db['encouragments']

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    # if msg.startswith()


client.run(os.getenv('TOKEN'))
