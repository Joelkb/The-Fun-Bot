from pyrogram import Client, filters
from info import START_IMG, HELP_IMG, LOOK_IMG, COMMAND_HAND_LER
from script import START_TXT, HELP_TXT, LOOK_TXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random 

tgbot=Client(
    "Pyrogram Bot",
    bot_token="5227324370:AAEVsHHyO3wDoH2sOH-bD_XD3GWrmLZXKv0",
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
    
@tgbot.on_message(filters.command("howilook"))
async def howilook_message(bot, message):
    await message.reply_photo(
            photo=random.choice(LOOK_IMG),
            caption=(LOOK_TXT),
            parse_mode='html'
)

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["roll", "dice"], COMMAND_HAND_LER)
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

tgbot.run()
