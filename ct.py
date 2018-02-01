#!/usr/bin/env python

import sys, json, requests
from collections import OrderedDict
from tabulate import tabulate

r = requests.get('https://api.coinmarketcap.com/v1/ticker/')

# data is the whole get as a list of dicts
data=r.json()

show_symbols=["BTC","ETH","BCH","LTC","DASH","XMR","MIOTA","ADA","BNB","CND","XVG","XRB","SC","XLM","TEL","NEO"]

symbol_list=[]

### sort data list of dictionaries by "name" 
d = sorted(data, key=lambda k: k['name']) 

### initialize empty table list
t=[]

for c in d:
    # every crypto entry is a dictionary
    name=c["name"]
    symbol=c["symbol"]
    price_usd=c["price_usd"]
    price_btc=c["price_btc"]
    # price_satoshi=float(price_btc)/0.00000001
    symbol_list.append(symbol)
    if symbol in show_symbols:
        # print ("%s, %s, %s, %s" % (name, symbol, price_usd, price_satoshi))
        # t.append([name, symbol, price_usd, price_satoshi])
        t.append([name, symbol, price_usd])

# print tabulate(t, headers=['Name', 'Symbol', 'Price_Usd', 'Price_Satoshi'], tablefmt='simple')
print tabulate(t, headers=['Name', 'Symbol', 'Price_Usd'], tablefmt='simple')

# uncomment to print all symbols
# print symbol_list
