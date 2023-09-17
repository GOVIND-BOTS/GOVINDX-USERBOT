# COPYRIGHT (C) 2021 BY GOVIND
"""
(((((((((((((((((((((((@GOVIND_OFFICIAl_MP0)))))))))))))))))))))))))))
(((((((((((((((((((((((@GOVIND_OFFICIAl_MP0)))))))))))))))))))))))))))
(((((((((((((((((((((((@GOVIND_OFFICIAl_MP0)))))))))))))))))))))))))))
(((((((((((((((((((((((@GOVIND_OFFICIAl_MP0)))))))))))))))))))))))))))
"""
# MADE BY GOVIND 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot.utils import admin_cmd as legendx
from userbot import bot as GOVIND
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("GOVIND", API_ID, API_HASH).start(bot_token=token)
pbot = Client("GOVIND", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "GOVIND USERBOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "GOVIND MP"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
LEGENDX = "[LEGEND X](https://t.me/GOVIND_USERBOT)"
VERSION = "3.1.5"
ID = 1100231654
REPO = "[GOVINDUSERBOT](https://github.com/GOVIND-BOTS/GOVINDX-USERBOT)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/GOVIND_USERBOT_SUPPORT)"
if __name__=="__main__":
  xbot.run_until_disconnected()

if __name__=="__main__":
  pbot.start()
  run()
