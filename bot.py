from pyrogram import Client
from info import SESSION, BOT_TOKEN, API_ID, API_HASH

tgbot=Client(
    name=SESSION,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=50,
    plugins={"root": "plugins"},
    sleep_threshold=5
)
