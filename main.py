from pyrogram import Client, filters
from info import START_IMG, HELP_IMG
from script import START_TXT, HELP_TXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

tgbot=Client(
    "Pyrogram Bot",
    bot_token="5024393552:AAERJgw_5mZ9csN5XBvnf8iZMzySfKg2lI4",
    api_id="8050217",
    api_hash="8a733396605cf07c31dfc79d7245270d"
)

@tgbot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
            photo=random.choice(START_IMG),
            caption=(START_TXT),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🍿 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ 🍿", url="t.me/filmy_harbour"),
                InlineKeyboardButton("🤴 Bot Owner 🤴", url="t.me/creatorbeatz")
            ],[InlineKeyboardButton("💥 Join our Main Channel 💥", url="https://t.me/+LJRsBp82HiJhNDhl")
            ]]
            ),
            parse_mode='html'
)

@tgbot.on_message(filters.command("help"))
async def help_message(bot, message):
    await message.reply_photo(
            photo=random.choice(HELP_IMG),
            caption=(HELP_TXT),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🍿 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ 🍿", url="t.me/filmy_harbour"),
                InlineKeyboardButton("🤴 Bot Owner 🤴", url="t.me/creatorbeatz")
            ],[InlineKeyboardButton("💥 Join our Main Channel 💥", url="https://t.me/+LJRsBp82HiJhNDhl")
            ]]
            ),
            parse_mode='html'
)

tgbot.run()
