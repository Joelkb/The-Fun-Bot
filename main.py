from pyrogram import Client, filters

tgbot=Client(
    "Pyrogram Bot",
    bot_token="5024393552:AAERJgw_5mZ9csN5XBvnf8iZMzySfKg2lI4"
    api_id="8050217"
    api_hash="8a733396605cf07c31dfc79d7245270d"
)

@tgbot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("👋 Hello I'am a test bot made by <a href='https://t.me/creatorbeatz'>JOEL</a>")

tgbot.run()
