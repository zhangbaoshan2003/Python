from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo_ochl('MSFT', start, today)
attributes=['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)
print(quotesdfMS[(quotesdfMS.high>50 and quotesdfMS.low<50)])
list = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list.append(y)
quotesdfMS.index = list
# quotesdfMS = quotesdfMS.drop(['date'], axis = 1)
list = []
quotesdfMS15 = quotesdfMS['15/01/01':'15/12/31']
for i in range(0, len(quotesdfMS15)):
    list.append(int(quotesdfMS15.index[i][3:5])) #get month just like '02'
quotesdfMS15['month'] = list
print(quotesdfMS15.groupby('month')['close'].mean())