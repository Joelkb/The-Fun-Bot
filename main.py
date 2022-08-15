from pyrogram import Client, filters, enums
from info import START_IMG, LOOK_IMG, MOVIE_PIC, COMMAND_HAND_LER, ADMINS, API_HASH, API_ID, BOT_TOKEN, MV_PIC, FSub_Channel, SESSION
from script import START_TXT, LOOK_TXT, HELP_TXT, ABOUT_TXT, SOURCE_TXT, MOVIE_ENG_TXT, MOVIE_MAL_TXT, OWNER_INFO, MV_TXT, KICKED, FSUB
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import UserNotParticipant, FloodWait, MessageNotModified
from plugins.fun_strings import FUN_STRINGS
from urllib.parse import quote
import random
import os
import asyncio

tgbot=Client(
    name=SESSION,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

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
    n = await message.reply_text("<b>Processing</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing.</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing..</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing...</b>")
    await asyncio.sleep(1)
    await n.delete()

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
            parse_mode=enums.ParseMode.HTML

)



@tgbot.on_message(filters.regex("movie") | filters.regex("Movie") & filters.group)
async def filter_handler(bot, message):
    if message.from_user.id not in ADMINS:
        await message.reply_photo(
            photo=(MOVIE_PIC),
            caption=(MOVIE_ENG_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('🇮🇳 Translate to Malayalam 🇮🇳', callback_data='movie_mal_txt')
                      ]]
            
            ),
            parse_mode=enums.ParseMode.HTML
)
    else:
        pro = await message.reply_text(f"<b>Hey {message.from_user.mention}, You are approved as Admin ✅</b>")
        await asyncio.sleep(5)
        await pro.delete()



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
                parse_mode=enums.ParseMode.HTML
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
                parse_mode=enums.ParseMode.HTML
            )
            await query.answer('Wᴇʟᴄᴏᴍᴇ Tᴏ Mʏ Hᴇʟᴘ Mᴏᴅᴜʟᴇ')

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
                parse_mode=enums.ParseMode.HTML
            )
            await query.answer("Wᴇʟᴄᴏᴍᴇ Tᴏ Mʏ Aʙᴏᴜᴛ Mᴏᴅᴜʟᴇ")

        elif query.data == "source":
            buttons = [[
                        InlineKeyboardButton('🔙 ʙᴀᴄᴋ', callback_data='about'),
                        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
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
                parse_mode=enums.ParseMode.HTML
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
                parse_mode=enums.ParseMode.HTML
            )

        elif query.data == "movie_mal_txt":
            btn = [[
                    InlineKeyboardButton("🇺🇲 Translate to English 🇺🇲", callback_data="movie_eng_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            try:
                if query.from_user.id == query.message.reply_to_message.from_user.id:
                    await query.message.edit_text(
                        text=(MOVIE_MAL_TXT.format(query.from_user.mention)),
                        reply_markup=reply_markup,
                        parse_mode=enums.ParseMode.HTML
                    )
                
                else:
                    await query.answer("This is not for you !", show_alert=True)
            except AttributeError:
                    await query.answer("Button Expired !", show_alert=True)

        elif query.data == "movie_eng_txt":
            btn = [[
                    InlineKeyboardButton("🇮🇳 Translate to Malayalam 🇮🇳", callback_data="movie_mal_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            try:
                if query.from_user.id == query.message.reply_to_message.from_user.id:
                    await query.message.edit_text(
                        text=(MOVIE_ENG_TXT.format(query.from_user.mention)),
                        reply_markup=reply_markup,
                        parse_mode=enums.ParseMode.HTML
                    )
                
                else:
                    await query.answer("This is not for you !", show_alert=True)
            except AttributeError:
                    await query.answer("Button Expired !", show_alert=True)

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
                parse_mode=enums.ParseMode.HTML
            )           

@tgbot.on_message(filters.command("howilook"))
async def howilook_message(bot, message):
    await message.reply_photo(
            photo=random.choice(LOOK_IMG),
            caption=(LOOK_TXT.format(message.from_user.first_name)),
            parse_mode=enums.ParseMode.HTML
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

@tgbot.on_inline_query()
async def inline(bot, query: InlineQuery):
    await query.answer(
        results = [
            InlineQueryResultArticle(
                title = "Movies",
                description = "For new and old movies and series in all languages, CLICK ME !",
                thumb_url = "https://telegra.ph/file/7c924bffb69a01d834ba4.jpg",
                input_message_content = InputTextMessageContent(
                    message_text = (MV_TXT)
                ),
                reply_markup = InlineKeyboardMarkup(
                [[
                  InlineKeyboardButton("ᴊᴏɪɴ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ", url="https://t.me/+5olNhPeyW31jYjBl"),
                  InlineKeyboardButton("ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+asOwq8hpxSgwOTY9")
               ],[
                  InlineKeyboardButton("ɴᴇᴡ ʀᴇʟᴇᴀsᴇs", url="https://t.me/+1Zr7U1TCCMw2YmJl")
                ]]
                )
            )
        ],
        cache_time = 0
    )

@tgbot.on_message(filters.command("trash") & filters.group)
async def trash_handler(bot, message):
    if message.from_user.id not in ADMINS:
        await message.reply_text("<b>Hey bro, This is an Admin Command !</b>")
    else:
        try:
            await message.reply_to_message.delete()
            await message.delete()
        except AttributeError:
            await message.reply_text("<b>Hey, Use this command as a reply to any message...</b>")

@tgbot.on_message(filters.command("calc"))
async def calculator(bot, message):
    oper = ['+', '-', '/', '*', '%']
    await message.reply_text(f"Hey {message.from_user.mention}, Give me the first number for your calculation.")
    x1=input
    await bot.send_message(message.chat.id, text="Okay!, Give me the second number for your calculation.")
    x2=input
    await bot.send_message(message.chat.id, text="Okay!, What operation do you want me to do?\nUse '+' for addition.\nUse '-' for substraction.\nUse '/' for division.\nUse '*' for multiplication.\nUse '%' for checking the reminder.")
    x3=input
    if x3 == '+':
        ans=x1+x2
        await bot.send_message(message.chat.id, text="Your answer is "+str(ans))
    elif x3 == '-':
        ans=x1-x2
        await bot.send_message(message.chat.id, text="Your answer is "+str(ans))
    elif x3 == '/':
        ans=x1/x2
        await bot.send_message(message.chat.id, text="Your answer is "+str(ans))
    elif x3 == '*':
        ans=x1*x2
        await bot.send_message(message.chat.id, text="Your answer is "+str(ans))
    elif x3 == '%':
        ans=x1%x2
        await bot.send_message(message.chat.id, text="Your answer is "+str(ans))
    elif x3 not in oper:
        await bot.send_message(message.chat.id, text="Please provide a valid operation.")
tgbot.run()
