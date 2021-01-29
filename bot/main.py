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
add_words = ['lose', 'victory']


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def get_key():
    date = datetime.datetime.now()
    key = str(date.month) + str(date.year) + str(date.day)
    return key


def add_value(value):
    key = get_key()
    if key in db.keys():
        stats = db[key]
        if value in stats.keys():
            stats[value] += 1
        else:
            stats[value] = 1
        db[key] = stats
    else:
        db[key] = {value: 1}


def get_stat(value):
    stats = {'lose': 0, 'victory': 0}
    if value == 'month':
        date = datetime.datetime.now()
        keys = db.prefix(str(date.month) + str(date.year))
        for key in keys:
            for key_ in db[key].keys():
                stats[key_] += db[key][key_]
        return f'''Your stats for this month
    Victories: {stats['victory']}
    Loses: {stats['lose']}    
    '''
    else:
        key = get_key()
        if key in db.keys():
            for key_ in db[key]:
                stats[key_] += db[key][key_]
        return f'''Your stats for this day
    Victories: {stats['victory']}
    Loses: {stats['lose']}    
    '''


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

    if msg.startswith('$add'):
        value = msg.split('add ', 1)[1]
        if value in add_words:
            add_value(value)
            await message.channel.send('Added')
        else:
            await message.channel.send(f'Look at your value. Must be as here: {add_words}')

    if msg.startswith('$stat'):
        string = ''
        if len(msg) > len('$stat'):
            value = msg.split('stat ', 1)[1]
            string = get_stat(value)
        else:
            string = get_stat('')
        await message.channel.send(string)

keep_alive()
client.run(os.getenv('TOKEN'))
