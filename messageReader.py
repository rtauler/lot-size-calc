#contract list list values
from contracts import contract_list

#import regular expressions
import re

def readMessage(a):

	#split signal string to array
	signal_arr = a.splitlines()


	#extract values of the signal array
	for i in signal_arr:
		#search for symbol
		if 'Instrument:' in i:
			symbol_original = i.split("Instrument: ",1)[1]
			symbol = symbol_original.lower()

		#Search for entry price
		if 'Entry' in i or 'entry' in i or 'EP' in i or 'Price' in i or 'price' in i:
			#print(i)
			entry_price = ''.join(re.findall("\d+\.\d+", i))
		
		#Search for Stop loss
		if 'Stop' in i or 'stop' in i or 'SL' in i:
			#print(i)
			stop_loss = ''.join(re.findall("\d+\.\d+", i))
		
		#Take profit 1
		if 'Target' in i or 'Tp1' in i:
			#print(i)
			take_profit_1 = ''.join(re.findall("\d+\.\d+", i))

		#Risk (no float value)
		if 'Risk' in i or 'risk' in i:
			#print(i)
			risk = ''.join(re.findall("\d", i))

	# print('SYM:	',symbol)
	# print('EP:	',entry_price)
	# print('SL:	',stop_loss)
	# print('TP1:	',take_profit_1)
	# print('RSK:	',risk)

	# print('-----')

	opList = [['SYM',symbol],['EP',entry_price],['SL',stop_loss],['TP1',take_profit_1],['RSK',risk]]

	return opList


# a = """Instrument: GBPJPY
# Order: BUY STOP
# Entry price: 150.82
# Stop Loss: 150.47
# Tp1: 151.18
# Tp2:151.75
# Recommended Risk: 1%
# RRR: 1:2

# Signal validity period: Good until cancelled"""

# readMessage(a)




