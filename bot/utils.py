import requests
import json
import datetime


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' - ' + json_data[0]['a']
    return quote


def get_key():
    date = datetime.datetime.now()
    key = str(date.month) + str(date.year) + str(date.day)
    return key


def clean_db(db):
    keys = db.keys()
    date = datetime.datetime.now()
    keys_ = db.prefix(str(date.month) + str(date.year))
    for key in keys:
        if key not in keys_:
            del db[key]
