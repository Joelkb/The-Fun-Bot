from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from script import MV_TXT


@Client.on_inline_query()
async def inline(bot, query: InlineQuery):
    await query.answer(
        results = [
            InlineQueryResultArticle(
                title = "Movies",
                description = "For new and old movies and series in all languages, CLICK ME !",
                thumb_url = "https://telegra.ph/file/7c924bffb69a01d834ba4.jpg",
                inputmessagecontent = InputTextMessageContent(
                    message_text = (MV_TXT)
                )
            )
        ],
        cache_time = 0
    )
