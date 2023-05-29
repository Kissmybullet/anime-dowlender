import os
from telethon import TelegramClient

api_id = os.environ.get('6212330')
api_hash = os.environ.get('1dcf154704672a8c279126e1ecf229c3')
bot_token = os.environ.get('6220163740:AAHQrDefHIVHM4OYwVEAQxYdNChAdeJ2y0k')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
