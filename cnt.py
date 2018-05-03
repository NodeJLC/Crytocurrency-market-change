import requests

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10000')
all_currencies = r.json()

cnt = 0
pos_neg = None
total = 0
for currency in all_currencies:
    percent_change = currency['percent_change_7d']
    if percent_change:
        cnt += 1
        total += float(percent_change)

avg = total / cnt

if avg > 0:
    pos_neg = "+"
else:
    pos_neg = "-"

print "The entire cryptocurrency market has fluctuated {0}{1}% in the last seven days".format(
    pos_neg, avg)