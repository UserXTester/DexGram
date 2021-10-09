"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name.**"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive`, {DEFAULTUSER} is Pro⚡..!\n\n"
                     
                     " |➖➖➖➖《Bot System》➖➖➖➖| \n"
                     f"`My Master`: **{DEFAULTUSER}**\n"
                     "`Dexgram`: **v1.0**\n"
                     "`Status`: **Online**\n"
                     "`Telethon`: **v1.23**\n"
                     "`Python`: **v3.9.8**\n"
                     "`GitHub`: **Connected**\n"
                     "`Heroku`: **Connected**\n"
                     "`Any Help` : @DexGram_Official\n
                     "`Bot By`: @Akki_ThePro\n\n"

                     "[Deploy DexGram](https://github.com/Akshat7678/DexGram)"
                     
