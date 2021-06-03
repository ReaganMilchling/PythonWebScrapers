import requests
import re

#You may or may not have to install requests, I find it easier than normal urlib
#py -m pip install requests
#Added regex to make my life easier
#I tried using beautiful soup for this but couldn't figure it out unfortunately

tickers = ["PLTR:NYSE", "AAPL:NASDAQ", "QCOM:NASDAQ", "GOOG:NASDAQ", "AMZN:NASDAQ"]
data = []
volume = []

def getData(s):
    site='https://www.google.com/finance/quote/' + s
    headers={'User-Agent':'Mozilla/5.0'}
    page = requests.get(site, headers=headers)
    text = page.text

    where = text.find('YMlKec fxKbKc')
    start = where
    end = start + 100
    data = text[start:end]
    
    x = re.findall("[\d]+[,]*[\d]+[.]+[\d]{2}", data)
    
    return x
def getVolume(s):
    site='https://www.google.com/finance/quote/' + s
    headers={'User-Agent':'Mozilla/5.0'}
    page = requests.get(site, headers=headers)
    text = page.text

    where = text.find('The average number of shares traded each day over the past 30 days')
    start = where
    end = start + 300
    data = text[start:end]
    
    x = re.findall("[\d]*[,]*[\d]*[.]*[\d]+[M]", data)
    
    return x

for i in range(len(tickers)):
    data.append(getData(tickers[i]))
    volume.append(getVolume(tickers[i]))
for i in range(len(tickers)):
    print(tickers[i] + ": ", data[i])
    print("Volume: ", volume[i])
