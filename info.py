from os import environ
import re
import os

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

START_IMG = (environ.get('START_IMG', 'https://telegra.ph/file/6a0726f79acd8300e9a04.jpg https://telegra.ph/file/d799c1a964f211028cc97.jpg https://telegra.ph/file/708a1d6ce805fcc6a46d0.jpg https://telegra.ph/file/85f95494565a762edb3e7.jpg https://telegra.ph/file/8c34c755dd16581c1c6b5.jpg https://telegra.ph/file/b987425b80bca0cf45c7e.jpg https://telegra.ph/file/2a8b3779760289b76de24.jpg https://telegra.ph/file/47961be968719b3e24cf0.jpg https://telegra.ph/file/2e127b0f6b1810d733c09.jpg https://telegra.ph/file/fcc849db4bf5c517f0f8d.jpg')).split()

LOOK_IMG = (environ.get('LOOK_IMG', 'https://telegra.ph/file/9fdd31655bc0ecf975a1f.jpg https://telegra.ph/file/f171f898a3674e67f2069.jpg https://telegra.ph/file/adcc01adc336d9d0b04c5.jpg https://telegra.ph/file/a5e39ea8f8b2970b78f47.jpg https://telegra.ph/file/7dd998a1ff3a1a208d1a5.jpg https://telegra.ph/file/47ed5746114960c2afde7.jpg https://telegra.ph/file/9c14458e8ea10667a3ead.jpg https://telegra.ph/file/b37f8512b3ed0c3b3a0f5.jpg https://telegra.ph/file/10f70f32175a99c89b375.jpg https://telegra.ph/file/4b390d9ca6b30e82523c2.jpg https://telegra.ph/file/eedca1e2ee069d64f12c7.jpg')).split()

COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

MOVIE_PIC = environ.get("MOVIE_PIC", "https://telegra.ph/file/3cdc36ae5925aa8fc2a50.jpg")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

API_ID = int(environ['API_ID'])

API_HASH = environ.get("API_HASH", "")

BOT_TOKEN = environ.get("BOT_TOKEN", "")

MV_PIC = environ.get("MV_PIC", "https://telegra.ph/file/7c924bffb69a01d834ba4.jpg")

FSub_Channel = environ.get("FSub_Channel", "")

SESSION = environ.get("SESSION", "") 

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
