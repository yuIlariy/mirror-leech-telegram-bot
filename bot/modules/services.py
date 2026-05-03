from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button(
        "Repo", "https://www.github.com/anasty17/mirror-leech-telegram-bot"
    )
    buttons.url_button("Code Owner", "https://t.me/xspes")
    reply_markup = buttons.build_menu(2)
    
    # Thumbnail photo
    photo_url = "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg"
    
    if await CustomFilters.authorized(_, message):
        start_string = f"""
**Welcome to the Mirror & Leech Bot!** 🚀

I can seamlessly mirror files from:
**Links | Telegram Files | Torrents | NZB | Rclone Cloud**
...directly to any Rclone cloud, Google Drive, or back to Telegram.

Type /{BotCommands.HelpCommand} to see a list of all available commands.
"""
        await message.reply_photo(
            photo=photo_url, 
            caption=start_string, 
            reply_markup=reply_markup
        )
    else:
        unauth_string = f"""
**Welcome to the Mirror & Leech Bot!** 🚀

I can mirror files from **Links | TG Files | Torrents | NZB | Rclone** to Google Drive, Telegram, or any Rclone cloud.

⚠️ **Access Denied:** You are not an authorized user! 
Please deploy your own mirror-leech bot to use these features.
"""
        await message.reply_photo(
            photo=photo_url, 
            caption=unauth_string, 
            reply_markup=reply_markup
        )


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
