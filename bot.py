import os

API_TOKEN = os.getenv("8138646021:AAEV8mZ-MFtpVgEN-_pFrRUAS4Qxt4fcCsQ")
ADMIN_ID = int(os.getenv("6619154186"))
#start command
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply("Hello, I'm alive!")
