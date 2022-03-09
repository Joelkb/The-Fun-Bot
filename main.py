from pyrogram import Client, filters
from info import START_IMG, LOOK_IMG, COMMAND_HAND_LER, MOVIE_PIC, ADMINS, API_HASH, API_ID, BOT_TOKEN
from script import START_TXT, LOOK_TXT, HELP_TXT, ABOUT_TXT, SOURCE_TXT, MAL_TRAN, HIN_TRAN, LANG, MOVIE_ENG_TXT, MOVIE_MAL_TXT, OWNER_INFO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import logging
import logging.config
import os
logger = logging.getLogger(__name__)

Client(
    "Pyrogram Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('FunBot.txt')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('logs'))
async def log_user(bot, message):
    await message.reply_text(
        text="This is an Admin command, Not for you!"
)

@Client.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
            photo=random.choice(START_IMG),
            caption=(START_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('sᴡɪᴛᴄʜ ʟᴀɴɢᴜᴀɢᴇ', callback_data='lang')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', url='https://t.me/filmy_harbour')
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            
            ),
            parse_mode='html'
)

@Client.on_message(filters.regex("movie") | filters.regex("Movie"))
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

@Client.on_callback_query()
async def cb_checker(bot, query: CallbackQuery):
        if query.data == "close_data":
            await query.message.delete()

        elif query.data == "start":
            buttons = [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('sᴡɪᴛᴄʜ ʟᴀɴɢᴜᴀɢᴇ', callback_data='lang')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', url='https://t.me/filmy_harbour')
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
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
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
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
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
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
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
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
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )
        elif query.data == "mal_tran":
            buttons = [[
                    InlineKeyboardButton('➕ എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ചേർക്കുക ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                ],[
                    InlineKeyboardButton('ഭാഷ മാറുക', callback_data='lang')
                ],[
                    InlineKeyboardButton('🤴ബോട്ട് ഉടമ🤴', callback_data="owner_info"),
                    InlineKeyboardButton('🍿സിനിമാ ഗ്രൂപ്പ്🍿', url='https://t.me/filmy_harbour')
                ],[
                    InlineKeyboardButton('ℹ️ സഹായം', callback_data='help'),
                    InlineKeyboardButton('😊 വിവരം', callback_data='about')
                ],[
                    InlineKeyboardButton('💥 ഞങ്ങളുടെ പ്രധാന ചാനലിൽ ചേരുക 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                  ]]
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(MAL_TRAN.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )
       
        elif query.data == "hin_tran":
            buttons = [[
                        InlineKeyboardButton('➕ मुझे अपने ग्रुप में जोड़ें ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('भाषा बदलें', callback_data='lang')
                     ],[
                        InlineKeyboardButton('🤴बॉट मालिक🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿फिल्म ग्रुप🍿', url='https://t.me/filmy_harbour')
                     ],[
                        InlineKeyboardButton('ℹ️ मदद', callback_data='help'),
                        InlineKeyboardButton('😊 विवरण', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 हमारे मुख्य चैनल से जुड़ें 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(HIN_TRAN.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )
            
        elif query.data == "lang":
            buttons = [[
                        InlineKeyboardButton('English', callback_data='start'),
                        InlineKeyboardButton('മലയാളം', callback_data='mal_tran'),
                        InlineKeyboardButton('हिन्दी', callback_data='hin_tran')
                      ]]
            await query.message.edit_text(
                text="⭗ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⭗ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⭗"
            )
            await query.message.edit_text(
                text="⦿ ⦿ ⦿"
            )
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(LANG),
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

@Client.on_message(filters.command("howilook"))
async def howilook_message(bot, message):
    await message.reply_photo(
            photo=random.choice(LOOK_IMG),
            caption=(LOOK_TXT.format(message.from_user.first_name)),
            parse_mode='html'
)

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@Client.on_message(
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


@Client.on_message(
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


@Client.on_message(
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

@Client.on_message(
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

@Client.on_message(
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

FUN_STRINGS = (
    "ഡാ നിന്റെ ഒക്കെ അമ്മയ്ക്കും പെങ്ങക്കും ഉള്ളതൊക്കെ തന്നാട എല്ലാർക്കും ഒള്ളത്.",
    "ഓ.. ധിക്കാരം... പഴേപോലെ തന്നെ....ഒരു മാറ്റോമില്ല.....ചുമ്മാതല്ല ഗതി പിടിക്കാത്തത്....!!!",
    "അള്ളാ... പിള്ളേരുടെ ഓരോ... പെഷനെ...",
    "എനിക്ക് എഴുതാൻ അല്ലെ അറിയൂ സാറേ.... വായിക്കാൻ അറിയില്ലല്ലോ....",
    "ഇന്ന് ഇനി നീ മിണ്ടരുത്... ഇന്നത്തെ കോട്ട കഴിഞ്ഞ്.....",
    "ചാരമാണെന്ന് കരുതി ചെകയാൻ നിൽക്കണ്ട കനൽ കെട്ടിട്ടില്ലെങ്കിൽ പൊള്ളും.",
    "ഒറ്റ ജീവിതമേ ഉള്ളു മനസിലാക്കിക്കോ, സ്വർഗ്ഗമില്ല നരകമില്ല, 'ഒറ്റ ജീവിതം', അത് എവിടെ എങ്ങനെ വേണമെന്ന് അവനവൻ തീരുമാനിക്കും",
    "വാട്ട് എ ബോംബെസ്റ്റിക് എക്സ്പ്ലോഷൻ! സച് എ ടെറിഫിക് ഡിസ്ക്ലോസ്!!",
    "ഗോ എവേ സ്ടുപ്പിഡ് ഇൻ ദി ഹൗസ് ഓഫ് മൈ വൈഫ്‌ ആൻഡ് ഡോട്ടർ യൂവിൽ നോട്ട് സി എനി മിനിറ്റ് ഓഫ് ദി ടുഡേ... ഇറങ്ങി പോടാ..",
    "ഐ കാൻ ഡു ദാറ്റ്‌ ഡു കാൻ ഐ ദാറ്റ്‌",
    "ക്രീം ബിസ്കറ്റിൽ ക്രീം ഉണ്ടന്ന് കരുതി ടൈഗർ ബിസ്കറ്റിൽ ടൈഗർ ഉണ്ടാകണമെന്നില്ല. പണി പാളും മോനെ...",
    "പട പേടിച്ചു പന്തളത്തു ചെന്നപ്പോ പന്തോം കുത്തി പട പന്തളത്തോട്ടെന്ന് പറഞ്ഞ പോലെ ആയല്ലോ.",
    "എന്റെ കർത്താവെ.... എന്നെ നീ നല്ലവനാകാൻ സമ്മതിക്കൂല്ല അല്ലെ.",
    "കാർ എൻജിൻ ഔട്ട് കംപ്ലീറ്റ്‌ലി......",
    "തള്ളെ കലിപ്പ് തീരണില്ലല്ലോ!!",
    "പാതിരാത്രിക്ക് നിന്റെ അച്ഛൻ ഉണ്ടാക്കി വെച്ചിരിക്കുന്നോ പൊറോട്ടയും ചിക്കനും....",
    "ഓ പിന്നെ നീ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് പ്രണയം.... നമ്മൾ ഒക്കെ പ്രേമിക്കുമ്പോൾ അത് കമ്പി....",
    "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ....",
    "അവളെ ഓർത്ത് കുടിച്ച കള്ളും നനഞ്ഞ മഴയും വേസ്റ്റ്....",
    "ഇത്രേം കാലം എവിടെ ആയിരുന്നു....!",
    "ഇൻഗ്ലീഷ് തീരെ പിടി ഇല്ല അല്ലെ....",
    "ഓൾ ദി ഡ്രീംസ്‌ ലൈക്‌ ട്വിങ്കിൽ സ്റ്റാർസ്...",
    "എന്റെ പ്രാന്തൻ മുത്തപ്പാ അവനെ ഒരു വഴിയാക്കി തരണേ",
    "പെങ്ങളെ കെട്ടിയ സ്ത്രീധന തുക തരുമോ അളിയാ",
    "നീ വല്ലാതെ ക്ഷീണിച്ചു പൊയി",
    "കണ്ണിലെണ്ണയൊഴിച്ചു കാത്തിരിക്കുവായിരുന്നളിയാ.",
    "ചെലക്കാണ്ട് എണീച്ച് പോടാ തടിയാ .\
    ഷട്ട് യുവർ മൗത് ബ്ലഡി ഗ്രാമവാസീസ്.",
    "പോയി ചാവട .\
    നിന്നെ കൊണ്ട് ചാവാൻ പറ്റുമോ.",
    "നിന്നെ കൊണ്ട് നാട്ടുകാർക്കും ഗുണോല്ല്യ വിട്ടുകാർക്കും ഗുണോല്ല്യ എന്തിനാ ഇങ്ങനെ നാണം കെട്ട് ജീവിക്കുന്നേട പട് വാഴെ ചെങ്കതളി വാഴ .", 
    "നീ ചായ അടിച്ചാൽ മതി എന്നെ അടിക്കണ്ട !",
    "സെൻസ് വേണം സെൻസിബിലിറ്റി വേണം സെൻസിറ്റിവിറ്റി വേണം",
    "നീ പോ മോനെ ദിനേശാ",
    "നിൻ്റെ തന്തയല്ല എൻ്റെ തന്ത",
    "കുറച്ച് കഞ്ഞിയെടുക്കട്ടെ?",
    "എൻ്റെ പിള്ളേരെ തൊടുന്നോടാ...",
    "പോയി ചത്തൂടെ, എന്തിനാ ഇങ്ങനെ ഭൂമിക്ക് ഭാരമായി ജീവിക്കുന്നത്...",
    "അതിന് നീ ഏതാ?...",
    "ഒന്ന് പോടെയ്, അവൻ fun ചോദിച്ച് വന്നേക്കുന്നു...",
    "ഇന്നാ ഈ bun തിന്നോ...",
    "അടിച്ച് മോളെ!",
    "വട്ടാണല്ലെ?...",
    "അങ്കമാലിയിലെ അമ്മാവൻ...",
    "എൻ്റെ ഗർഭം ഇങ്ങനല്ല...",
    "എന്താടോ വാര്യരെ ഞാൻ നന്നാവാത്തെ?...",
)


@Client.on_message(
    filters.command("fun", COMMAND_HAND_LER)
)
async def runs(_, message):
    """ /fun strings """
    effective_string = random.choice(FUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

self.run()
