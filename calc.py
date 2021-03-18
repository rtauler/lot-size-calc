#contract list list values
from contracts import contract_list

win_ratio = 2

#inptus for user
symbol = input('Symbol?\n')
balance = float(input('Balance?\n'))
risk = float(input('Risk?\n'))
op_type = input('Operation Type? (buy/sell)\n')
entry_price = float(input('Entry price?\n'))
stop_loss = float(input('Stop Loss?\n'))
man_tp = input('Take Profit? (optional)\n')
man_lot = input('Lot? (optional)\n')

#fixed variables based on the user input
ammount_at_risk = (risk*0.01) * balance
ammount_to_win = ammount_at_risk * win_ratio

#Difference between entry and stop loss, also the tp
if(op_type == "buy"):
	diff_e_sl = entry_price - stop_loss
	tp = round((diff_e_sl * win_ratio) + entry_price,5)

elif(op_type == "sell"):
	diff_e_sl = stop_loss - entry_price
	tp = round((diff_e_sl * win_ratio) - entry_price,5)
	#make nnumber absolute (take out the '-')
	tp = abs(tp)

#ignore generated Take profit if Take profit is inputed manually from the user
if man_tp != "":
	tp = float(man_tp)

#iterate through the list to get the contract and genrate the number of pips
for i in contract_list:

	if symbol == i[0]:
		sl_pips = diff_e_sl * i[1]

#----

#get the recommended lot
#if lot is inputed manually use the one inputed by the user
if man_lot != "":
	rec_lot = float(man_lot)
else:
	rec_lot = ammount_at_risk/sl_pips


#get the roundup lot
rec_lot_round = round(rec_lot, 2)

#get projected amm to risk & win
proj_amm_risk = round((rec_lot_round * sl_pips), 2)
proj_amm_win = round(((rec_lot_round * sl_pips)) * win_ratio, 2)

#get projected % risk
proj_risk = round(proj_amm_risk/balance,2)*100

#------

#define a min viable lot for when the recommended lot is smaller 
#than 0.01 but still want to trade at least 0.01
min_lot = 0.01

#get min amm to risk & win
min_amm_risk = round((min_lot * sl_pips), 2)
min_amm_win = round(((min_lot * sl_pips)) * win_ratio, 2)

#get min % risk
min_risk = round(min_amm_risk/balance,2)*100

#-----

#check if operation is OK, neutral or KO
#if both recommended lot and rounded lot are over 0.01 its OK
if rec_lot >= 0.01 and rec_lot_round >= 0.01:
	op_stat = 'OK'

#if recommended is less than 0.01 but rounded is at least equal NEUTRAL
elif rec_lot < 0.01 and rec_lot_round >= 0.01:
	op_stat = 'NEUTRAL'

#if below 0.01 not recommended to operate (min position at 0.01 given below!)
elif rec_lot < 0.01 and rec_lot_round < 0.01:
	op_stat = 'KO' 

print('GENERATED OPERATION is:',op_stat, '\n',
	'-----------------------------------\n',
	'Symbol:		',symbol,'\n',
	'Account Balance:	',balance,'$\n',
	'User inputed Risk:	',risk,'%\n',
	'Operation type:	',op_type,'\n',
	'Entry Price:		',entry_price,'$\n',
	'Stop Loss:		',stop_loss,'$\n',
	'Take Profit:		',tp,'$\n',
	'-----------------------------------\n',
	'Recommended lot:	',round(rec_lot,3),'\n',
	'Roundup lot:		',rec_lot_round,'\n',
	'-----------------------------------\n',
	'Project. risk:		',proj_risk,'%\n',
	'Project. amm risk:	',proj_amm_risk,'$\n',
	'Project. amm win:	',proj_amm_win,'$\n',
	'-----------------------------------\n',
	'Min viab. lot:		',min_lot,'\n',
	'Min viab. risk:	',min_risk,'%\n',
	'Min viab. amm risk:	',min_amm_risk,'$\n',
	'Min viab. amm win:	',min_amm_win,'$\n',
	'-----------------------------------\n'
	)