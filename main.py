#importing libs

import asyncio
import sqlite3

#starting db
connection = sqlite3.connect("test12.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        nick TEXT NOT NULL,
        isadmin INTEGER NOT NULL
    )
""")

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters

bot = Bot(token="5947987351:AAGnAgt00HcM7usENY3GC7B1IZtze9_Zp0o")
dp = Dispatcher(bot=bot)


count = 1
def CreateUser(cmd):
    cm = []
    for item in cmd:
        if cmd[0] != item:
            cm.append(item)

    name = cm[0]
    isadmin = int(cm[1])
    glob = globals()
    count = glob["count"]
    cursor.execute(f"""
    INSERT INTO Users(id, nick, isadmin) VALUES({count}, '{name}', {isadmin})
    """)
    glob["count"] += 1

def PrintUsers(cmd) :
    cursor.execute("""
    SELECT * FROM Users
    """)
    data = cursor.fetchall()
    return data

commands = {
    "/create_user": CreateUser,
    "/print_users": PrintUsers
}

@dp.message_handler(filters.Text(contains="/", ignore_case=True))
async def test(message: Message):
    cmd = message.text.strip().split();
    result = commands[cmd[0]](cmd)
    if cmd[0] == "/print_users":
        for item in result:
            message.reply(text=str(item))

@dp.message_handler()
async def test(message: Message):
    await message.reply(message.text)


asyncio.run(
    dp.start_polling()
)
