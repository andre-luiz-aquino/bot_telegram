from os import getenv
from pyrogram import Client, filters
from dotenv import load_dotenv
from func import  btc

load_dotenv()

app = Client(
    'dashbordbtcbot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)


@app.on_message(filters.command('btc'))
async def messages(Client, message):
        await message.reply(btc)
        
        
app.run()