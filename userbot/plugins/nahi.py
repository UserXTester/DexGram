# Coded By Zylern.
"""
Show different synonyms of nope
Syntax: .nahi

"""
from telethon import events
import os
import sys
import random, re
import asyncio
from uniborg.util import admin_cmd
from telethon import events


@borg.on(admin_cmd(pattern="nahi ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    x=(random.randrange(1,11)) 
    if (x==1):
      await event.edit("**Nahi**")
    if (x==2):
      await event.edit("**Naa**")
    if (x==3):
      await event.edit("**No**")
    if (x==4):
      await event.edit("**Nope**")
    if (x==5):
      await event.edit("**Bola na nahi**")
    if (x==6):
      await event.edit("**Bilkul Nahi**")
    if (x==7):
      await event.edit("**Nop**")
    if (x==8):
      await event.edit("**Nah**")
    if (x==9):
      await event.edit("**Nai**")
    if (x==10):
      await event.edit("**Nahi Bhai**")      
      
      
