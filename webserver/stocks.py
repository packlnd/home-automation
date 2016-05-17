from yahoo_finance import Share, Currency
import json

usdsek = Currency("USDSEK")

def get_stocks():
    data = None
    with open('stocks.json') as f:
        data = json.load(f)
    populate_prices(data)
    return data

def populate_prices(data):
    usdsek.refresh()
    tot = 0.0
    for i in range(len(data["stocks"])):
        t = get_today(data["stocks"][i])
        data["stocks"][i]["today"] = t
        tot += t
    data["total"] = tot

def get_today(stock):
    s = Share(stock["quote"])
    sw = float(usdsek.get_rate())
    val = float(stock["amount"])*(float(s.get_price()) - float(s.get_open()))
    if stock["curr"] == "USD":
        val *= sw
    return val

