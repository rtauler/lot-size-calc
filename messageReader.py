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
			#remove the "/" if necessary that divides the currencies sometimes
			if '/' in i:
				i = re.sub('/', '', i)

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
		if 'Target' in i or 'Tp1' in i or 'TP1' in i:
			#print(i)
			take_profit_1 = ''.join(re.findall("\d+\.\d+", i))

		#Risk (no float value)
		if 'Risk' in i or 'risk' in i:
			#print(i)
			risk = ''.join(re.findall("\d", i))


	#create list
	opList = {'Symbol':symbol,'EntryPrice':entry_price,'StopLoss':stop_loss,'TakeProfit1':take_profit_1,'Risk':risk}

	return opList






