from yahoo_finance import Currency
import json
import ystockquote as ysq

def get_stocks():
    data = None
    with open('stocks.json') as f:
        data = json.load(f)
    populate_prices(data)
    return data

def populate_prices(data):
    tot = 0.0
    for i in range(len(data["stocks"])):
        t = get_today(data["stocks"][i])
        data["stocks"][i]["today"] = t
        tot += t
    data["total"] = tot

def get_today(stock):
    #usdsek = Currency("USDSEK")
    print str(stock["quote"])
    s = ysq.get_price(str(stock["quote"]))
    #sw = float(usdsek.get_rate())
    print s
    #val = float(stock["amount"])*(float(s.get_price()) - float(s.get_open()))
    #if stock["curr"] == "USD":
    #    val *= sw
    #return val
    return 2
