import requests
from config import *

from plotly.graph_objs import Bar
from plotly import offline

url = "https://stock-data-yahoo-finance-alternative.p.rapidapi.com/v6/finance/quote"
querystring = {"symbols":"FB,AAPL,AMZN,NFLX,GOOG"}

# Make API call and store the response.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }
r = requests.get(url, headers=headers, params=querystring)

# Process results.
data = r.json()

stock_list, price_list = [], []

# Iterate through 'result' list and add stock symbols
# to stock_list
for each in data['quoteResponse']['result']:
    stock_list.append(each['symbol'])

for each in data['quoteResponse']['result']:
    price_list.append(each['regularMarketPrice'])

# Make visualization.
vis_data = [{
    'type': 'bar',
    'x': stock_list,
    'y': price_list,
}]

my_layout = {
    'title': 'FAANG Stock Prices',
    'xaxis': {'title': 'Stock Symbol'},
    'yaxis': {'title': 'Stock Price'},
}

fig = {'data': vis_data, 'layout': my_layout}
offline.plot(fig, filename='yahoo_stock_chart.html')