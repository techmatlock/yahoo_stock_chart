import requests
from config import *

url = "https://stock-data-yahoo-finance-alternative.p.rapidapi.com/v6/finance/quote"

querystring = {"symbols":"FB,AAPL,AMZN,NFLX,GOOG"}

# Make API call and store the response.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'x-rapidapi-host': "stock-data-yahoo-finance-alternative.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }
r = requests.get(url, headers=headers, params=querystring)

# Process results and store as dictionary.
data = r.json()