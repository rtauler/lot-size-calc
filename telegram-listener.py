import re
from telethon import TelegramClient, events, sync

#API info
api_id = 3215739
api_hash = '2ae75dcac0528a9fa786523608d96c3e'


client = TelegramClient('session_read', api_id, api_hash)

#L2T VIP CHANNEL:
#user_input_channel = -1001389726384
#TESTING
user_input_channel = 'me'

subjectFilter = 'Instrument' and 'Stop Loss'

#listen to messages from target channel
@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
	#Get message text
	newMessage = event.message.message
	#check if message contains the two keywords defined in subjectFilter
	if subjectFilter in newMessage:
		print(newMessage)


#infinite loop
with client:
	client.run_until_disconnected()