from pyrogram import Client, filters
from info import START_IMG, LOOK_IMG, COMMAND_HAND_LER, MOVIE_PIC, ADMINS, API_HASH, API_ID, BOT_TOKEN, MV_PIC, FSub_Channel, SESSION
from script import START_TXT, LOOK_TXT, HELP_TXT, ABOUT_TXT, SOURCE_TXT, MOVIE_ENG_TXT, MOVIE_MAL_TXT, OWNER_INFO, MV_TXT, KICKED, FSUB, COMMAND_USER, REPORT_TXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant
from plugins.fun_strings import FUN_STRINGS
import random
import logging
import logging.config
import os
import asyncio
logger = logging.getLogger(__name__)


tgbot=Client(
    session_name=SESSION,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


@tgbot.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        if message.from_user.id not in ADMINS:
            await message.reply_text(COMMAND_USER.format(message.from_user.mention))
        else:
            await message.reply_document('FunBot.log')
    except Exception as e:
        await message.reply(str(e))

@tgbot.on_message(filters.command("start"))
async def start_message(bot, message):
    if FSub_Channel:
        try:
            user = await bot.get_chat_member(FSub_Channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text(KICKED.format(message.from_user.mention))
                return
        except UserNotParticipant:
            await message.reply_text(
                text=(FSUB.format(message.from_user.mention)),
                reply_markup=InlineKeyboardMarkup(
                  [[
                    InlineKeyboardButton("Join Our Updates Channel 📢", url=f"t.me/{FSub_Channel}")
                 ],[
                    InlineKeyboardButton("Try Again 🔄", url="t.me/the_fun_mallu_bot?start")
                  ]]
                )
            )

            return

    await message.reply_photo(
            photo=random.choice(START_IMG),
            caption=(START_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', callback_data="movie_grp")
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            
            ),
            parse_mode='html'

)



@tgbot.on_message(filters.regex("movie") | filters.regex("Movie"))
async def filter_handler(bot, message):
    await message.reply_photo(
            photo=(MOVIE_PIC),
            caption=(MOVIE_ENG_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('🇮🇳 Translate to Malayalam 🇮🇳', callback_data='movie_mal_txt')
                      ]]
            
            ),
            parse_mode="html"
)



@tgbot.on_callback_query()
async def cb_checker(bot, query: CallbackQuery):
        if query.data == "close_data":
            await query.message.delete()

        elif query.data == "start":
            buttons = [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', callback_data="movie_grp")
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(START_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "help":
            buttons = [[
                          InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='start'),
                          InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                      ],[
                          InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data'),
                          InlineKeyboardButton('❤️ sᴏᴜʀᴄᴇ', callback_data='sourcehelp')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(HELP_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "about":
            buttons = [[
                          InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='start'),
                          InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help')
                      ],[
                          InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data'),
                          InlineKeyboardButton('❤️ sᴏᴜʀᴄᴇ', callback_data='source')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(ABOUT_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "source":
            buttons = [[
                        InlineKeyboardButton('🔙 ʙᴀᴄᴋ', callback_data='about'),
                        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "sourcehelp":
            buttons = [[
                        InlineKeyboardButton('🔙 ʙᴀᴄᴋ', callback_data='help'),
                        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "owner_info":
            btn = [[
                    InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start"),
                    InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", url="t.me/creatorbeatz")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=(OWNER_INFO),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "movie_mal_txt":
            btn = [[
                    InlineKeyboardButton("🇺🇲 Translate to English 🇺🇲", callback_data="movie_eng_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=(MOVIE_MAL_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )
        elif query.data == "movie_eng_txt":
            btn = [[
                    InlineKeyboardButton("🇮🇳 Translate to Malayalam 🇮🇳", callback_data="movie_mal_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=(MOVIE_ENG_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "movie_grp":
            btn = [[
                    InlineKeyboardButton("ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ", url="https://t.me/+5olNhPeyW31jYjBl"),
                    InlineKeyboardButton("ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+asOwq8hpxSgwOTY9")
                 ],[
                    InlineKeyboardButton("ɴᴇᴡ ʀᴇʟᴇᴀsᴇs", url="https://t.me/+1Zr7U1TCCMw2YmJl"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_data")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.reply_photo(
                photo=(MV_PIC),
                caption=(MV_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )
            
        elif query.data == "report":
            await query.answer(REPORT_TXT.format(query.from_user.first_name), show_alert=True)
            

@tgbot.on_message(filters.command("howilook"))
async def howilook_message(bot, message):
    await message.reply_photo(
            photo=random.choice(LOOK_IMG),
            caption=(LOOK_TXT.format(message.from_user.first_name)),
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

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["throw", "dart"], COMMAND_HAND_LER)
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["goal", "shoot"], COMMAND_HAND_LER)
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
PIN_BALL = "🎳"
# EMOJI CONSTANTS

@tgbot.on_message(
    filters.command(["pinball", "tenpin"])
)
async def pinball_tenpin(client, message):
    """ /pinball an @animatedpinball """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=PIN_BALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@tgbot.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@tgbot.on_message(
    filters.command("fun", COMMAND_HAND_LER)
)
async def runs(_, message):
    """ /fun strings """
    effective_string = random.choice(FUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

@tgbot.on_message(filters.regex("@admin") | filters.regex("@admins"))
async def admin_handler(bot, message):
    admins = await message.reply_sticker(
            sticker='CAACAgUAAxkBAAEEMnhiNA722UYMtilQ36wzPU1QTWLZ7gACqQADyJRkFOv8RlMxwyrKIwQ',
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton("✅ REPORT SENT ✅", callback_data="report")
                      ]]
            )
)
    await asyncio.sleep(20)
    await admins.delete()
    await message.delete()

tgbot.run()
