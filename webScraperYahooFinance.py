import requests
import re

#You may or may not have to install requests, I find it easier than normal urlib
#py -m pip install requests 
#Added regex to make my life easier

tickers = ["PLTR", "AAPL", "DIS", "TSLA", "CRSR", "INTC", "QCOM", "GOOG", "AMZN"]
price = []
volume = []

def priceData(s):
    site='https://finance.yahoo.com/quote/' + s
    headers={'User-Agent':'Mozilla/5.0'}
    page = requests.get(site, headers=headers)
    text = page.text

    #print(page.status_code)
    where = text.find('Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)')
    start = where + 61
    end = start + 8
    data = text[start:end]

    x = re.findall("[\d]+[,]*[\d]+[.]+[\d]{2}", data)
    
    return x

def volumeData(s):
    site='https://finance.yahoo.com/quote/' + s
    headers={'User-Agent':'Mozilla/5.0'}
    page = requests.get(site, headers=headers)
    text = page.text

    where = text.find('TD_VOLUME-value')
    start = where
    end = start + 200
    data = text[start:end]
    
    x = re.findall("[\d]*[,]*[\d]*[,]*[\d]+[,]{1}[\d]{3}", data)
    
    return x

for i in range(len(tickers)):
    volume.append(volumeData(tickers[i]))
    price.append(priceData(tickers[i]))
for i in range(len(tickers)):
    print(tickers[i] + ": ", price[i])
    print("Volume: ", volume[i])

