import json
import requests
import re

#Same as the others, requests was easier to understand and documentation was better
#This might not always work, bloomberg is harder to scrape than yahoo but I should be accessing the free api correctly
#not sure if this counts as web scraping but its the only way I could find to get the intra stock data automatically
ticker = "INTC"
ticker2 = "SPY"
ticker3 = "AAPL"
days = "1"
interval = "60"

def getData(ticker, days, interval):
    site = "https://www.bloomberg.com/markets2/api/intraday/{}%3AUS?days={}&interval=2&volumeInterval={}&currency=USD".format(ticker, days, interval)

    headers={'User-Agent':'Mozilla/5.0'}
    page = requests.get(site, headers=headers)
        
    data = page.json()
    
    return data


#could change the below to txt, but that is impossible to read. Open my jsonReader(atatched) to view easily
with open('{}{}daysdata.json'.format(ticker2, days), 'w') as outfile:
    json.dump(getData(ticker2, days, interval), outfile)
