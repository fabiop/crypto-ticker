# crypto-ticker
Crypto Coin Ticker


Usage:

```
git clone https://github.com/fabiop/crypto-ticker.git
while true; crypto-ticker/ct.py ; sleep 300 ; done
```

300 is seconds, updates every 5 minutes 

If you want timestamps, install ts, ie 

on Ubuntu
```
apt-get install moreutils
```

on MacOS 
```
brew install ts
```

then run:

```
while true; do echo -n "------------------"; echo|ts ; crypto-ticker/ct.py ; sleep 300 ; done
```


Example on MacOS here: https://imgur.com/a/66scw 

Enjoy! :)
