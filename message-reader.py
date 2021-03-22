#contract list list values
from contracts import contract_list

#import regular expressions
import re



#import the signal raw text
signal_raw = open("usdcad", "r")

signal_str = signal_raw.read()

#iterate through all contract list to check if the signal contains one of them

#split signal string to array
signal_arr = signal_str.splitlines()


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

print('SYM:	',symbol)
print('EP:	',entry_price)
print('SL:	',stop_loss)
print('TP1:	',take_profit_1)
print('RSK:	',risk)




