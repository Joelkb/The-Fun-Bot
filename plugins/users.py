from database.sql import add_user, query_msg, full_userbase
from pyrogram import filters, Client as Bot
from script import WAIT_MSG
from info import ADMINS

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")
