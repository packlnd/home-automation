from yahoo_finance import Currency
import json
import ystockquote as ysq
from datetime import datetime
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
    #usdsek = Currency("USDSEK")
    now = datetime.now(); then = now.subtract(days=5)
    hist = ysq.get_historical_prices(stock["quote"], now.strftime("%Y-%m-%d"), then.strftime("%Y-%m-%d"))
    ret = {}
    for day in hist:
        ret[day] = float(stock["amount"])*(float(hist[day]['Close']) - float(Hist[day]['Open']))
    return ret
