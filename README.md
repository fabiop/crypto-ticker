# crypto-ticker
Crypto Coin Ticker for *nix type terminals


Usage:

```
git clone https://github.com/fabiop/crypto-ticker.git
while true; do crypto-ticker/ct.py ; sleep 300 ; done
```

300 is seconds, updates every 5 minutes 


You may need to install some modules:
```
pip install json requests collections tabulate
```

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
alias ticker='while true; do echo|ts ; crypto-ticker/ct.py ; sleep 300 ; done'
ticker
```

Example running on MacOS here: https://imgur.com/a/pM2dg

Enjoy! :)
