from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

_zmq = DWX_ZeroMQ_Connector()

# // OP_BUY = 0
# // OP_SELL = 1
# // OP_BUYLIMIT = 2
# // OP_SELLLIMIT = 3
# // OP_BUYSTOP = 4
# // OP_SELLSTOP = 5

def makeOrder(action,Otype,symbol,price,sl,tp,comment,lot,magic,ticket):
	
	if Otype == 'BUY':
		Otype = 4
	elif Otype == 'SELL':
		Otype = 5

	_my_trade = {
	'_action': action, 
	'_type': Otype,
	'_symbol': symbol, 
	'_price': price, 
	'_SL': sl, 
	'_TP': tp, 
	'_comment': comment, 
	'_lots': lot, 
	'_magic': magic, 
	'_ticket': ticket}

	#print(_my_trade)

	#print('ORDER EXECUTED:',_my_trade)

	_zmq._DWX_MTX_NEW_TRADE_(_order=_my_trade)

