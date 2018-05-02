import pandas as pd
from decimal import Decimal

crypto = 'ETH'
quote = 'BTC'

newCandlestick = {'e': 'kline', 'E': 1525019854523, 's': 'ETHBTC', 'k': {'t': 1525019820000, 'T': 1525019879999, 's': 'ETHBTC', 'i': '1m', 'f': 57326037, 'L': 57326183, 'o': '0.07282300', 'c': '0.07290700', 'h': '0.07293300', 'l': '0.07279800', 'v': '48.57300000', 'n': 147, 'x': False, 'q': '3.53912310', 'V': '25.57800000', 'Q': '1.86451044', 'B': '0'}}
print('\nNew candlestick for {}/{}'.format(crypto, quote))
df = pd.DataFrame([newCandlestick['k']])
df['t'] = pd.to_datetime(df['t'], unit='ms')
df['T'] = pd.to_datetime(df['T'], unit='ms')
print(df.to_string(justify='center', columns=['t','T','o','c','h','l','v','q','n'], header=['ts from','ts to','open','close','high','low','vol ' + crypto,'vol ' + quote, 'trade nb'],  formatters={'t': lambda x: x.strftime("%H:%M:%S"), 'T': lambda x: x.strftime("%H:%M:%S")}))

allCandleStick = [{'t': 1525019820000, 'T': 1525019879999, 's': 'ETHBTC', 'i': '1m', 'f': 57326037, 'L': 57326112, 'o': '0.07282300', 'c': '0.07281400', 'h': '0.07289000', 'l': '0.07279800', 'v': '21.14500000', 'n': 147, 'x': False, 'q': '1.54092264', 'V': '17.09800000', 'Q': '1.24622675', 'B': '0'}, {'t': 1525019880000, 'T': 1525019939999, 's': 'ETHBTC', 'i': '1m', 'f': 57326037, 'L': 57326113, 'o': '0.07282300', 'c': '0.07288100', 'h': '0.07289000', 'l': '0.07279800', 'v': '21.21700000', 'n': 77, 'x': False, 'q': '1.54617007', 'V': '17.17000000', 'Q': '1.25147418', 'B': '0'}, {'t': 1525019940000, 'T': 1525019999999, 's': 'ETHBTC', 'i': '1m', 'f': 57326037, 'L': 57326121, 'o': '0.07282300', 'c': '0.07288100', 'h': '0.07289000', 'l': '0.07279800', 'v': '28.97300000', 'n': 85, 'x': False, 'q': '2.11106139', 'V': '17.59400000', 'Q': '1.28237594', 'B': '0'}]
print('\nCandlesticks for {}/{}'.format(crypto, quote))
df = pd.DataFrame(allCandleStick)
df['t'] = pd.to_datetime(df['t'], unit='ms')
df['T'] = pd.to_datetime(df['T'], unit='ms')
print(df.to_string(justify='center', columns=['t','T','o','c','h','l','v','q','n'], header=['ts from','ts to','open','close','high','low','vol ' + crypto,'vol ' + quote, 'trade nb'], formatters={'t': lambda x: x.strftime("%H:%M:%S"), 'T': lambda x: x.strftime("%H:%M:%S")}))

fullOrderBook = {'bids': {Decimal('0.07288200'): Decimal('9.00000000'), Decimal('0.07287200'): Decimal('1.77600000'), Decimal('0.07285500'): Decimal('0.08300000'), Decimal('0.07284700'): Decimal('10.30000000'), Decimal('0.07284600'): Decimal('6.84800000'), Decimal('0.07281800'): Decimal('0.63000000'), Decimal('0.07281700'): Decimal('1.09800000'), Decimal('0.07281500'): Decimal('0.23800000'), Decimal('0.07281400'): Decimal('19.41000000'), Decimal('0.07281000'): Decimal('0.33800000'), Decimal('0.07280600'): Decimal('0.23500000'), Decimal('0.07280400'): Decimal('0.04100000'), Decimal('0.07280100'): Decimal('0.30200000'), Decimal('0.07279500'): Decimal('0.64000000'), Decimal('0.07279400'): Decimal('1.02300000'), Decimal('0.07279300'): Decimal('0.40700000'), Decimal('0.07278900'): Decimal('0.12800000'), Decimal('0.07278500'): Decimal('0.08200000'), Decimal('0.07278100'): Decimal('9.70000000'), Decimal('0.07277500'): Decimal('0.05900000'), Decimal('0.07276500'): Decimal('0.31100000'), Decimal('0.07276300'): Decimal('0.10000000'), Decimal('0.07276100'): Decimal('0.38300000'), Decimal('0.07275300'): Decimal('0.13700000'), Decimal('0.07275100'): Decimal('0.19200000'), Decimal('0.07275000'): Decimal('0.57600000'), Decimal('0.07274300'): Decimal('13.00000000'), Decimal('0.07273600'): Decimal('0.80000000'), Decimal('0.07272900'): Decimal('0.43800000'), Decimal('0.07272700'): Decimal('1.10800000'), Decimal('0.07272600'): Decimal('0.41600000'), Decimal('0.07272500'): Decimal('0.10900000'), Decimal('0.07272400'): Decimal('1.33500000'), Decimal('0.07272300'): Decimal('0.27500000'), Decimal('0.07272100'): Decimal('0.76800000'), Decimal('0.07272000'): Decimal('25.49200000'), Decimal('0.07271800'): Decimal('1.02300000'), Decimal('0.07271700'): Decimal('0.09700000'), Decimal('0.07271600'): Decimal('0.71100000'), Decimal('0.07271300'): Decimal('0.15000000'), Decimal('0.07271100'): Decimal('0.67100000'), Decimal('0.07270800'): Decimal('0.06000000'), Decimal('0.07270200'): Decimal('4.49000000'), Decimal('0.07270100'): Decimal('1.52500000'), Decimal('0.07270000'): Decimal('9.67900000'), Decimal('0.07269300'): Decimal('3.00000000'), Decimal('0.07268900'): Decimal('0.40600000'), Decimal('0.07267000'): Decimal('14.07700000'), Decimal('0.07264500'): Decimal('0.04200000'), Decimal('0.07264000'): Decimal('0.31000000'), Decimal('0.07263900'): Decimal('1.70700000'), Decimal('0.07263700'): Decimal('0.01400000'), Decimal('0.07262700'): Decimal('0.29100000'), Decimal('0.07261400'): Decimal('0.49100000'), Decimal('0.07261100'): Decimal('6.14500000'), Decimal('0.07261000'): Decimal('28.09100000'), Decimal('0.07260000'): Decimal('10.00000000'), Decimal('0.07259200'): Decimal('23.80000000'), Decimal('0.07258300'): Decimal('0.41000000'), Decimal('0.07257900'): Decimal('1.79300000'), Decimal('0.07257200'): Decimal('0.13600000'), Decimal('0.07255700'): Decimal('2.75600000'), Decimal('0.07255000'): Decimal('0.67400000'), Decimal('0.07254800'): Decimal('0.13800000'), Decimal('0.07254600'): Decimal('0.45600000'), Decimal('0.07253600'): Decimal('2.00000000'), Decimal('0.07253500'): Decimal('0.01400000'), Decimal('0.07252000'): Decimal('8.43200000'), Decimal('0.07251300'): Decimal('0.01400000'), Decimal('0.07250600'): Decimal('0.13800000'), Decimal('0.07250500'): Decimal('0.13800000'), Decimal('0.07250000'): Decimal('12.48000000'), Decimal('0.07249900'): Decimal('0.95200000'), Decimal('0.07248700'): Decimal('0.41400000'), Decimal('0.07248200'): Decimal('0.41400000'), Decimal('0.07247100'): Decimal('0.41400000'), Decimal('0.07247000'): Decimal('0.27600000'), Decimal('0.07246900'): Decimal('0.82800000'), Decimal('0.07246600'): Decimal('0.01400000'), Decimal('0.07246500'): Decimal('0.06800000'), Decimal('0.07246300'): Decimal('0.04200000'), Decimal('0.07246100'): Decimal('38.61900000'), Decimal('0.07245900'): Decimal('1.30000000'), Decimal('0.07243800'): Decimal('0.58700000'), Decimal('0.07243100'): Decimal('0.20000000'), Decimal('0.07295100'): Decimal('0.10100000'), Decimal('0.07295300'): Decimal('0.15000000'), Decimal('0.07295400'): Decimal('5.17100000'), Decimal('0.07295600'): Decimal('0.04900000'), Decimal('0.07296100'): Decimal('0.35300000'), Decimal('0.07296500'): Decimal('0.33000000'), Decimal('0.07296600'): Decimal('0.01600000'), Decimal('0.07296900'): Decimal('0.01800000'), Decimal('0.07297100'): Decimal('0.10400000'), Decimal('0.07297200'): Decimal('0.05700000'), Decimal('0.07297300'): Decimal('1.02300000'), Decimal('0.07297500'): Decimal('10.23600000'), Decimal('0.07298100'): Decimal('0.02000000'), Decimal('0.07298200'): Decimal('0.04700000'), Decimal('0.07298300'): Decimal('0.14200000'), Decimal('0.07298700'): Decimal('0.12100000'), Decimal('0.07298900'): Decimal('0.12700000'), Decimal('0.07299000'): Decimal('0.04300000'), Decimal('0.07299100'): Decimal('1.02400000'), Decimal('0.07299400'): Decimal('0.04100000'), Decimal('0.07299600'): Decimal('0.25000000'), Decimal('0.07300000'): Decimal('46.55700000'), Decimal('0.07300500'): Decimal('0.08500000'), Decimal('0.07300900'): Decimal('0.11200000'), Decimal('0.07301000'): Decimal('0.60000000'), Decimal('0.07301100'): Decimal('1.02300000'), Decimal('0.07301600'): Decimal('0.04100000'), Decimal('0.07301800'): Decimal('0.02800000'), Decimal('0.07302000'): Decimal('0.11200000'), Decimal('0.07302100'): Decimal('0.27700000'), Decimal('0.07302200'): Decimal('0.10000000'), Decimal('0.07302700'): Decimal('0.13900000'), Decimal('0.07303000'): Decimal('0.31900000'), Decimal('0.07303300'): Decimal('0.06300000'), Decimal('0.07303500'): Decimal('0.46800000'), Decimal('0.07303600'): Decimal('1.02300000'), Decimal('0.07303900'): Decimal('0.30000000'), Decimal('0.07304600'): Decimal('0.04100000'), Decimal('0.07304700'): Decimal('0.08200000'), Decimal('0.07304900'): Decimal('58.55200000'), Decimal('0.07305000'): Decimal('3.63000000'), Decimal('0.07305300'): Decimal('4.26600000'), Decimal('0.07305700'): Decimal('0.03200000'), Decimal('0.07306200'): Decimal('0.06000000'), Decimal('0.07306300'): Decimal('0.04200000'), Decimal('0.07306400'): Decimal('0.03200000'), Decimal('0.07306500'): Decimal('0.47300000'), Decimal('0.07306700'): Decimal('1.34600000'), Decimal('0.07307500'): Decimal('0.06900000'), Decimal('0.07307900'): Decimal('0.05600000'), Decimal('0.07308100'): Decimal('20.22100000'), Decimal('0.07308200'): Decimal('0.43800000'), Decimal('0.07308300'): Decimal('0.01600000'), Decimal('0.07308400'): Decimal('0.12000000'), Decimal('0.07309100'): Decimal('0.01600000'), Decimal('0.07309200'): Decimal('0.30200000'), Decimal('0.07309300'): Decimal('0.08900000'), Decimal('0.07309700'): Decimal('0.01500000'), Decimal('0.07309900'): Decimal('0.95500000'), Decimal('0.07310000'): Decimal('2.91000000'), Decimal('0.07310100'): Decimal('0.09300000'), Decimal('0.07310300'): Decimal('0.64600000'), Decimal('0.07310400'): Decimal('8.43800000'), Decimal('0.07310500'): Decimal('0.93700000'), Decimal('0.07310900'): Decimal('1.78100000'), Decimal('0.07311000'): Decimal('0.29900000'), Decimal('0.07311100'): Decimal('0.03200000'), Decimal('0.07311300'): Decimal('0.76300000'), Decimal('0.07311500'): Decimal('0.33900000'), Decimal('0.07311700'): Decimal('0.01500000'), Decimal('0.07312000'): Decimal('0.13600000'), Decimal('0.07312200'): Decimal('0.01600000'), Decimal('0.07312300'): Decimal('0.68300000'), Decimal('0.07312600'): Decimal('0.02800000'), Decimal('0.07312700'): Decimal('0.08300000'), Decimal('0.07312800'): Decimal('0.27700000'), Decimal('0.07313100'): Decimal('0.04200000'), Decimal('0.07313400'): Decimal('2.00000000'), Decimal('0.07313600'): Decimal('2.25400000'), Decimal('0.07314000'): Decimal('0.24100000'), Decimal('0.07314700'): Decimal('6.84800000'), Decimal('0.07314900'): Decimal('0.24100000'), Decimal('0.07315000'): Decimal('0.12200000'), Decimal('0.07315200'): Decimal('0.01800000'), Decimal('0.07315300'): Decimal('0.03200000'), Decimal('0.07315400'): Decimal('0.20400000'), Decimal('0.07315500'): Decimal('5.78700000'), Decimal('0.07315600'): Decimal('0.06500000'), Decimal('0.07315900'): Decimal('0.04200000'), Decimal('0.07316000'): Decimal('0.05500000'), Decimal('0.07316100'): Decimal('0.41100000'), Decimal('0.07316200'): Decimal('0.29800000'), Decimal('0.07316500'): Decimal('0.83000000'), Decimal('0.07316700'): Decimal('0.41200000'), Decimal('0.07316800'): Decimal('0.06900000'), Decimal('0.07317000'): Decimal('0.52200000'), Decimal('0.07317300'): Decimal('0.37200000'), Decimal('0.07317400'): Decimal('0.15900000'), Decimal('0.07317600'): Decimal('0.17000000'), Decimal('0.07317700'): Decimal('0.21700000'), Decimal('0.07280800'): Decimal('5.47800000'), Decimal('0.07282900'): Decimal('60.88800000'), Decimal('0.07110400'): Decimal('1.40600000'), Decimal('0.07110000'): Decimal('1.47900000'), Decimal('0.07205500'): Decimal('1.03500000'), Decimal('0.07281100'): Decimal('0.10000000'), Decimal('0.07274800'): Decimal('3.63000000'), Decimal('0.07288900'): Decimal('0.39700000'), Decimal('0.07280900'): Decimal('0.10000000'), Decimal('0.07217000'): Decimal('0.71700000'), Decimal('0.07280000'): Decimal('6.95800000'), Decimal('0.07250200'): Decimal('0.41400000'), Decimal('0.07289500'): Decimal('0.33000000'), Decimal('0.07288500'): Decimal('15.13000000'), Decimal('0.07237000'): Decimal('215.88400000'), Decimal('0.07220300'): Decimal('0.83100000'), Decimal('0.07290000'): Decimal('0.75700000'), Decimal('0.07285600'): Decimal('2.28000000'), Decimal('0.07284800'): Decimal('8.03500000'), Decimal('0.07283800'): Decimal('0.85000000'), Decimal('0.07283000'): Decimal('0.05600000'), Decimal('0.07236200'): Decimal('8.30500000'), Decimal('0.07260300'): Decimal('8.99700000'), Decimal('0.07290100'): Decimal('13.72500000'), Decimal('0.07267700'): Decimal('2.03000000'), Decimal('0.07290300'): Decimal('6.86300000'), Decimal('0.07270300'): Decimal('0.05600000'), Decimal('0.07142600'): Decimal('0.14000000'), Decimal('0.07136300'): Decimal('1.26100000'), Decimal('0.07290700'): Decimal('13.20000000'), Decimal('0.07124900'): Decimal('0.14000000'), Decimal('0.07107200'): Decimal('0.16900000'), Decimal('0.07290800'): Decimal('0.36900000')}, 'asks': {Decimal('0.07302000'): Decimal('0.11200000'), Decimal('0.07303900'): Decimal('1.32400000'), Decimal('0.07311500'): Decimal('0.33900000'), Decimal('0.07327600'): Decimal('0.04900000'), Decimal('0.07333500'): Decimal('19.44900000'), Decimal('0.07310400'): Decimal('6.43800000'), Decimal('0.07331000'): Decimal('1.61200000'), Decimal('1.00000000'): Decimal('27.16500000'), Decimal('0.07300800'): Decimal('0.10000000'), Decimal('0.07355500'): Decimal('4.95900000'), Decimal('0.07310500'): Decimal('2.69700000'), Decimal('0.07299600'): Decimal('0.01400000'), Decimal('0.07300000'): Decimal('44.14700000'), Decimal('0.07306700'): Decimal('0.54600000'), Decimal('0.07308500'): Decimal('58.55200000'), Decimal('0.07315500'): Decimal('0.19800000'), Decimal('0.07339000'): Decimal('0.84200000'), Decimal('0.07350000'): Decimal('24.83700000'), Decimal('0.07297900'): Decimal('0.67200000'), Decimal('0.07299100'): Decimal('0.30000000'), Decimal('0.07300400'): Decimal('0.10000000'), Decimal('0.07303500'): Decimal('0.21000000'), Decimal('0.07311200'): Decimal('0.25800000'), Decimal('0.07309200'): Decimal('1.10200000'), Decimal('0.07325100'): Decimal('0.05600000'), Decimal('0.07700000'): Decimal('107.29200000'), Decimal('0.07299900'): Decimal('0.10800000'), Decimal('0.07351900'): Decimal('6.55000000'), Decimal('0.07297700'): Decimal('0.46100000'), Decimal('0.07301800'): Decimal('0.02800000'), Decimal('0.07359600'): Decimal('0.33000000'), Decimal('0.07297600'): Decimal('1.04300000'), Decimal('0.07397600'): Decimal('0.21000000')}}
print('\nFull order book for {}/{}'.format(crypto, quote))
listOfBidTuples = [x for x in fullOrderBook['bids'].items()]
df = pd.DataFrame(listOfBidTuples)
print('\nBids')
print(df.to_string())

listOfAskTuples = [x for x in fullOrderBook['asks'].items()]
df = pd.DataFrame(listOfAskTuples)
print('\nAsks')
print(df.to_string())