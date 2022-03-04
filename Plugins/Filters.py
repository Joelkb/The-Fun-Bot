from pyrogram import Client, filters
from info import MOVIE_PIC
from scrypt import MOVIE_ENG_TXT

@Client.on_message(filters.regex("movie"))
async def filter_handler(bot, message):
    await message.reply_photo(
        photo=(MOVIE_PIC),
        caption=(MOVIE_ENG_TXT),
        parse_mode="html"
    )
