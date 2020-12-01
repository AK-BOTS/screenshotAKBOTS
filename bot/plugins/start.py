from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Projec Group', url='https://t.me/AV_BOTS'),
                    InlineKeyboardButton('Project Channel', url='https://t.me/Bot_Gram_Developers')
                ],
                [
                    InlineKeyboardButton('My Father', url='https://t.me/kannaadiga')
                ]
            ]
        )
    )
