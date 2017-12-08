#!/usr/bin/env python

import sys, json, requests

r = requests.get('https://api.coinmarketcap.com/v1/ticker/')

# data is the whole get as a list of dicts
data=r.json()

show_symbols=["BTC","ETH","BCH","LTC","DASH","XMR","MIOTA","ADA"]

# Header
# print ("%s, %s, %s, %s" % ("Name", "Symbol", "Price_Usd", "Price_Btc"))

symbol_list=[]

for c in data:
    # every crypto entry is a dictionary
    name=c["name"]
    symbol=c["symbol"]
    price_usd=c["price_usd"]
    price_btc=c["price_btc"]
    symbol_list.append(symbol)
    if symbol in show_symbols:
        # print ("%s, %s, %s, %s" % (name, symbol, price_usd, price_btc))
        print ("%s, %s, USD %s" % (name, symbol, price_usd))

# uncomment to print all symbols
# print symbol_list
