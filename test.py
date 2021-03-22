#contract list list values
from contracts import contract_list

#import the signal raw text
signal_raw = open("eurusd", "r")

signal_str = signal_raw.read()

#iterate through all contract list to check if the signal contains one of them

print(signal_str)

print('----------')


#iterate through the list of contracts
for i in contract_list:

	#check if capitalizad iterating index of contract list exists in the signal text
	if i[0].upper() in signal_str:
		symbol = i[0]
		print(symbol)

	
