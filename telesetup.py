#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("An online StringSession generator Made With ReplRun")

print("Telethon (docs.telethon.dev)")
print("Telethon UserBot")

print("Select your required option: ")
s_l = input("enter y / n ? ?? ")

if s_l == "y":

	from telethon.sync import TelegramClient
	from telethon.sessions import StringSession
	APP_ID = int(input("Enter APP ID here: "))
	API_HASH = input("Enter API HASH here: ")
	with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
		session_str = client.session.save()
		s_m = client.send_message("me", session_str)
		s_m.reply(
		   " This StringSession is generated using https://repl.it/@AkshatKumar6/DexGram ! \n Please subscribe @Dexgram_Official FOR Any Help Or Support"
		   )
		print(
		    "please check your Telegram Saved Messages for the StringSession ")

elif s_l == "n":
	print(
	    "No problem if u don't want to run this session then  why did you clicked on this link you Idiot if you have done a mistake! just refresh the page and try again!"
	)
else:
	print("please select only y / n !!, ")

