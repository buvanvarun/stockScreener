import pandas as pd

from alpha_vantage.timeseries import TimeSeries

import time

from decouple import config

API_KEY = config('key')

ts = TimeSeries(key=API_KEY,output_format='pandas')

data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min',outputsize='full')
# print(data)

# i = 1
# while i==1:
#     data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min',outputsize='full')
#     data = pd.DataFrame(data)
#     data.to_excel("output.xlsx")
#     time.sleep(60)

close_data = data['4. close']
percent_change = close_data.pct_change()
last_change = percent_change[-1]

if abs(last_change) > 0.0004:
    print("MSFT alert")

# print(percent_change)

