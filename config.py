import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID', "22469064")
api_hash = os.environ.get('API_HASH', "c05481978a217fdb11fa6774b15cba32")
bot_token = os.environ.get('BOT_TOKEN', "7401282886:AAHWvkih1IZbMvGaBoG1Bx08Dw3d9nSNtVI")

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
