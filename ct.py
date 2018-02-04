#!/usr/bin/env python

import sys, json, requests, csv
from collections import OrderedDict
from tabulate import tabulate

r = requests.get('https://api.coinmarketcap.com/v1/ticker/')

# data is the whole get as a list of dicts
data=r.json()

# Import portfolio csv file
with open('portfolio.csv', 'rb') as f:
    reader = csv.reader(f)
    po = list(reader)

# convert list into dict with k=name[0] v=[rest of list]
pod={}
for i in po:
    try:
        pod[i[0]]=i[1:]
    except:
        pass

# show_symbols=["BTC","ETH","BCH","LTC","DASH","XMR","MIOTA","ADA","BNB","CND","XVG","XRB","SC","XLM","TEL","NEO"]
show_symbols = [ i[0] for i in po ]

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
        quantity=pod[symbol][0]
        usdtotal=float(quantity)*float(price_usd)
        t.append([name, symbol, price_usd, quantity, usdtotal])

# portfolio grand total
pgt=0
for i in t:
    pgt=pgt+i[4]

# print tabulate(t, headers=['Name', 'Symbol', 'Price_Usd', 'Price_Satoshi'], tablefmt='simple')
print(tabulate(t, headers=['Name', 'Symbol', 'Price_Usd','Quantity','Usd_Total'], tablefmt='simple'))
print("Portfolio Grand Total(USD): %s" % (pgt))

# uncomment to print all symbols
# print symbol_list
