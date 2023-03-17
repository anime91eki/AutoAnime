import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 25654389)) #API ID
API_HASH = environ.get('API_HASH', '89d5973b8325a5a800e515eabc8c6d5e') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', 'Your Bot Token') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'Your MongoDb') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 5009250822)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001854781135))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL',-1001863366316))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID',1026) ) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
