# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98)
# Update Channel @Digital_Botz & @DigitalBotz_Support

"""
Apache License 2.0
Copyright (c) 2022 @RknDeveloper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/RknDeveloper
Repo Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot
License Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot/blob/main/LICENSE
"""

from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "25599491"))
    API_HASH = getenv("API_HASH", "c8e3c0561cf148a6504f27b111fc3698")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
 
    FORCE_SUB = int(getenv("FORCE_SUB", "-1002053727982"))
    ADMIN = list(map(int, getenv("ADMIN", "5983189506").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002037384930"))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://cdn.prod.website-files.com/6462655e6f1811aabe80d8bd/665c8d03c23393fe530a63f3_Top%2010%20Telegram%20channel%20bots-3.png")
    
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://envs.sh/AGr.jpg").split()
    
    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
