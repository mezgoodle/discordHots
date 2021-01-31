<h1 id="project-title" align="center">
  discordHots <img alt="logo" width="40" height="40" src="https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png" /><br>
  <img alt="language" src="https://img.shields.io/badge/language-python-brightgreen?style=flat-square" />
  <img alt="language" src="https://img.shields.io/github/issues/mezgoodle/discordHots?style=flat-square" />
  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/mezgoodle/discordHots?style=flat-square" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mezgoodle/discordHots?style=flat-square" />
  <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/mezgoodle/discordHots?style=flat-square" />
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mezgoodle/discordHots?style=flat-square">
</h1>

<p align="center">
🌟Hello everyone! This is the repository of my <i>Discord</i> bot on Python.🌟
</p>

<h2 align="center">
  <i>Table of contents</i>
</h2>

- [Motivation 🎖️](#motivation-)
- [Build status 🏗️](#build-status-)
- [Badges 🏅](#badges-)
- [Code style 📇](#code-style-)
- [Screenshots 📷](#screenshots-)
- [Tech/framework used 🔧](#techframework-used-)
- [Features 💪](#features-)
- [Code Example ✍️](#code-example-)
- [Installation 💻](#installation-)
- [Fast usage 💨](#fast-usage-)
- [API Reference 🦾](#api-reference-)
- [Tests 🧪](#tests-)
- [Contribute 💁🏻](#contribute-)
- [Credits 🧑‍🤝‍🧑](#credits-)
- [License 🔖](#license-)

## Motivation 🎖️

At first, I saw [this](https://www.youtube.com/watch?v=SPTfmiYiuok&feature=emb_logo) video from **freeCodeCamp** and [this](https://tproger.ru/video/boty-dlja-discord-na-python-proekt-dlja-nachinajushhih/) article from **Tproger**. Also I like to play [HotS](https://heroesofthestorm.com/en-us/) with my friends every day. So I thought if we can log our statistic of games.

## Build status 🏗️

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

![Test Code](https://github.com/mezgoodle/discordHots/workflows/Test%20Code/badge.svg)

## Badges 🏅

Other badges

[![Theme](https://img.shields.io/badge/Theme-Bot-brightgreen?style=flat-square)](https://www.google.com.ua/)
[![Platform](https://img.shields.io/badge/Platform-Discord-brightgreen?style=flat-square)](https://www.google.com.ua/)

## Code style 📇

I'm using [Codacy](https://www.codacy.com/) to automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/96180c20b781457d8a754b20b814cc41)](https://www.codacy.com/gh/mezgoodle/discordHots/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/discordHots&amp;utm_campaign=Badge_Grade)
 
## Screenshots 📷

- Inspire method

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots1.png)

- Stat method for day

![Screenshot 2](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots2.png)

- Stat method for month

![Screenshot 3](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots3.png)

- Add method

![Screenshot 4](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots4.png)

- Updated stat method for day

![Screenshot 5](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots5.png)

- Clear method

![Screenshot 6](https://raw.githubusercontent.com/mezgoodle/images/master/discordHots6.png)

## Tech/framework used 🔧

**Built with**

- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [requests](https://requests.readthedocs.io/en/master/)
- [replit](https://pypi.org/project/replit/)
- [datetime](https://docs.python.org/3/library/datetime.html)

## Features 💪

With my bot you can **inspire** yourself, and **keep statistics** of your games. Also it is easy to expand opportunities.

## Code Example ✍️

`utils.py`

```python
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
```

## Installation 💻

1. Clone this repository:

```
git clone https://github.com/mezgoodle/discordHots.git
```

2. Rename `.env_sample` to `env` and replace variable:

```
TOKEN=<YOUR_DISCORD_BOT_TOKEN>
```

3. Install dependencies:

```
pip install -r requirements.txt
```

or

```
poetry install
```

## Fast usage 💨

Type in terminal:

```
python bot/main.py
```

## Tests 🧪

I made tests only for [utils.py](https://github.com/mezgoodle/discordHots/blob/master/bot/utils.py) [here](https://github.com/mezgoodle/discordHots/blob/master/test/test_utils.py). The result you can see [here](https://github.com/mezgoodle/discordHots/actions).

## Contribute 💁🏻

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/discordHots/blob/master/CONTRIBUTING.md).

## Credits 🧑‍🤝‍🧑

Links which inspired me to build this project:

- [Article](https://tproger.ru/video/boty-dlja-discord-na-python-proekt-dlja-nachinajushhih/)
- [Video](https://www.youtube.com/watch?v=SPTfmiYiuok&feature=emb_logo)

## License 🔖

MIT © [mezgoodle](https://github.com/mezgoodle)
