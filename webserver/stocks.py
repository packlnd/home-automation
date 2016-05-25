from yahoo_finance import Currency
import json
import ystockquote as ysq
from datetime import datetime, timedelta
from collections import defaultdict

def get_stocks():
    data = None
    with open('stocks.json') as f:
        data = json.load(f)
    res = populate_prices(data)
    return res

def populate_prices(data):
    res = defaultdict(lambda: 0)
    for i in range(len(data["stocks"])):
        t = get_today(data["stocks"][i])
        for day in t:
            res[day] += t[day]
    return res

def get_today(stock):
    now = datetime.now(); then = now - timedelta(days=5)
    ret = {}
    usdsek = float(Currency("USDSEK").get_bid())
    try:
        print repr(str(stock["quote"]))
	hist = ysq.get_historical_prices(str(stock["quote"]), then.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d"))
    	for day in hist:
            ret[day] = float(stock["amount"])*(float(hist[day]['Close']) - float(hist[day]['Open']))
            if stock["curr"] == "USD":
                ret[day] *= usdsek
    except Exception as e:
        print e
        print "Couldnt find information for %s" % stock["quote"]
    return ret
