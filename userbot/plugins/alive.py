"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://t.me/DexGram/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive, My Pro master..!` {DEFAULTUSER}\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     # Below is Important Things..
                     "`Bot created by:` [NubDexter](tg://user?id=440510599)\n"
                     f"`My Master`: {DEFAULTUSER}\n\n"
                     "[Deploy this userbot Now](https://github.com/NubDexter/DexGram)\n"
                     
