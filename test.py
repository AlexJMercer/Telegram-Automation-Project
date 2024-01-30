# Import Stuff

import os
import random
import time
from keep_alive import keep_alive

from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync
from telethon import functions, types


api_id = '24354845'
api_hash = 'a74f2687430622c5a79a015dbf2912da'
user_id = '6285534669'
phone_number = '+918285944852'
mask_phone = "+918511402867"

client = TelegramClient('session_name', api_id, api_hash)
client.start()


# send a message to a contact
@client.on(events.NewMessage(chats=mask_phone))
async def my_event_handler(event):
    message = event.message.message
    print(message)
    if message == "hi":
        await client.send_message(mask_phone, "hello sir, this is a test message.")
    elif message == "bye":
        await client.send_message(mask_phone, "bye sir, this is a test message.")
    else:
        await client.send_message(mask_phone, "I don't understand sir, this is a test message.")

keep_alive()
client.run_until_disconnected()