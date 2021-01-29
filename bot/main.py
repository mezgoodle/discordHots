from utils import get_key, get_quote, clean_db
from keepAlive import keep_alive
from replit import db
import datetime
import os
import discord
from dotenv import load_dotenv

load_dotenv()


client = discord.Client()
add_words = ['lose', 'victory']


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
    clean_db(db)
    stats = {'lose': 0, 'victory': 0}
    if value == 'month':
        date = datetime.datetime.now()
        keys = db.prefix(str(date.month) + str(date.year))
        for key in keys:
            for key_ in db[key].keys():
                stats[key_] += db[key][key_]
        winrate = int(stats['victory']) / \
            (int(stats['victory']) + int(stats['lose']))
        return f'''Your stats for this month
    Victories: {stats['victory']}
    Loses: {stats['lose']}
    Winrate: {winrate}
    '''
    else:
        key = get_key()
        if key in db.keys():
            for key_ in db[key]:
                stats[key_] += db[key][key_]
        winrate = int(stats['victory']) / \
            (int(stats['victory']) + int(stats['lose']))
        return f'''Your stats for this day
    Victories: {stats['victory']}
    Loses: {stats['lose']}
    Winrate: {winrate}
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
