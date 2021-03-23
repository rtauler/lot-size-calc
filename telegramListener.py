import re
from telethon import TelegramClient, events, sync

from messageReader import readMessage
from calc import calcLot

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
		print('----ORIGINAL MSG-------')
		print(newMessage)
		#extract the data of the message into a list
		print('----EXTRACTED DATA-----')
		extData = readMessage(newMessage)
		print(extData)
		#extract the specifics in the list
		print('----CALCULATED LOT-----')
		for i in extData:
			if 'SYM' == i[0]:
				symbol = i[1]
			elif 'EP' == i[0]:
				entry_price = i[1]
			elif 'SL' == i[0]:
				stop_loss = i[1]
			elif 'TP1' == i[0]:
				man_tp = i[1]
			elif 'RSK' == i[0]:
				risk = i[1]

		#calculate the lot size
		opLot = calcLot(symbol,float(750),float(risk),float(2),float(entry_price),float(stop_loss),man_tp,'')
		print(opLot)

		print('---JOINED LIST------')

		op = extData + opLot

		print(op)

#infinite loop to keep listening the channel
with client:
	client.run_until_disconnected()