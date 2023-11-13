import time
import requests
import pandas as pd
import datetime
while(1):
   #response = requests.get ('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
   #print (response.text)
  
   book = {}
   response = requests.get ('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
   book = response.json()
  
   data = book['data']
  
   #print (data)
  
   bids = (pd.DataFrame(data['bids'])).apply(pd.to_numeric,errors='ignore')
   bids.sort_values('price', ascending=False, inplace=True)
   bids = bids.reset_index(); del bids['index']
   bids['type'] = 0
  
   asks = (pd.DataFrame(data['asks'])).apply(pd.to_numeric,errors='ignore')
   asks.sort_values('price', ascending=True, inplace=True)
   asks['type'] = 1
  
   df = bids.append(asks)
  
   df['timestamp'] = pd.to_datetime('now')
  
   print (df)
  
   df.to_csv("2023-11-11-bithumb-BTC-orderbook.csv", mode='a', header=False, index=False)
  
   time.sleep(1)

  
#print (response.status_code)
