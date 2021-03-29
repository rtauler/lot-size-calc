from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

_zmq = DWX_ZeroMQ_Connector()

def openOrder(symbol,lot):
	_my_trade = {
	'_action': 'OPEN', 
	'_type': 0,
	'_symbol': symbol, 
	'_price': 0.0, 
	'_SL': 250, 
	'_TP': 750, 
	'_comment': 'PythTrader', 
	'_lots': lot, 
	'_magic': 123456, 
	'_ticket': 0}

	#print(_my_trade)

	_zmq._DWX_MTX_NEW_TRADE_(_order=_my_trade)

