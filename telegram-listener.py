import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)

api_id = 3215739
api_hash = '2ae75dcac0528a9fa786523608d96c3e'

client = TelegramClient('session_read', api_id, api_hash)

# Here you define the target channel that you want to listen to:

#REAL
# user_input_channel = 'https://t.me/signalstestsmithers1'
#REAL

#TESTING
user_input_channel = 'me'
#TESTING

subjectFilter = 'Instrument' and 'Stop Loss'

#listen to messages from target channel
@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
	#Get message text
	newMessage = event.message.message
	#print(newMessage)

	if subjectFilter in newMessage:
		print(newMessage)



with client:
	client.run_until_disconnected()