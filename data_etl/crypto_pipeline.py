# ETL Pipeline for extracting historical prices of BTC and ETH using web scraping from coinmarketcap.com

# Libraries used in ETL
import pandas as pd
import datetime
import requests
import bs4
from bs4 import BeautifulSoup

# Sets todays/last years' date using datetime
day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year
last_year = year - 1

# Todays date
start = datetime.datetime(last_year, month, day).strftime('%Y-%m-%d')
# Last year from todays date
end = datetime.datetime.now().strftime('%Y-%m-%d')

# Formatting dates to the query parameters of the URL for API call
starting = str(year)+'0'+str(month)+''+str(day)
ending = str(last_year)+'0'+str(month)+''+str(day)

# API Request
r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={}&end={}'.format(ending,starting))

# Using BeautifulSoup Library, extract data in HTML Format
soup = bs4.BeautifulSoup(r.text, "html.parser")
btc_price = float(soup.findAll('span', {'class': "h2 text-semi-bold details-panel-item--price__value"})[0].text)
btc_change = soup.findAll('span', attrs={'data-format-percentage': True})[0].text
container = soup.findAll('tr', {'class': 'text-right'})

# Initialize our Pandas Dataframe
index = []
columns = []
data = pd.DataFrame()

# Number of items initialized (0 Indexed)
n = len(container) - 1

# Extract the historical prices of Bitcoin by date into our Dataframe
for c in container:
    index.append(c.findChildren()[0].text)
    columns.append(c.findChildren()[4].text)

# Initialize and clean our dataframe labels
data['date'] = index
data['price'] = columns
data.index = data['date']
data.drop(columns='date', inplace=True)
data = data.iloc[::-1]

# Calculates the weekly, monthly, and yearly moving averages of prices
data['maw'] = data['price'].rolling(7).mean()
data['mam'] = data['price'].rolling(30).mean()
data['maa'] = data['price'].rolling(n).mean()

btc_maw = round(data.iloc[n]['maw'],2)
btc_mam = round(data.iloc[n]['mam'],2)
btc_maa = round(data.iloc[n]['maa'],2)

# Web scraping from coinmarketcap.com to extract historical prices of Ethereum

# API Request
r = requests.get('https://coinmarketcap.com/currencies/ethereum/historical-data/?start={}&end={}'.format(ending,starting))

# Using BeautifulSoup Library, extract data in HTML Format
soup = bs4.BeautifulSoup(r.text, "html.parser")
eth_price = float(soup.findAll('span', {'class': "h2 text-semi-bold details-panel-item--price__value"})[0].text)
eth_change = soup.findAll('span', attrs={'data-format-percentage': True})[0].text
container = soup.findAll('tr', {'class': 'text-right'})

# Number of items initialized (0 Indexed)
n = len(container) - 1

# Re-initialize our Pandas Dataframe
index = []
columns = []
data = pd.DataFrame()

# Extract the historical prices of Ethereum by date into our Dataframe
for c in container:
    index.append(c.findChildren()[0].text)
    columns.append(c.findChildren()[4].text)

# Initialize and clean our dataframe labels
data['date'] = index
data['price'] = columns
data.index = data['date']
data.drop(columns = ['date'], inplace=True)
data = data.iloc[::-1]

# Calculates the weekly, monthly, and yearly moving averages of prices
data['maw'] = data['price'].rolling(7).mean()
data['mam'] = data['price'].rolling(30).mean()
data['maa'] = data['price'].rolling(n).mean()

eth_maw = round(data.iloc[n]['maw'],2)
eth_mam = round(data.iloc[n]['mam'],2)
eth_maa = round(data.iloc[n]['maa'],2)

# Load our BTC/ETH data into a Python Dictionary
crypto = {
    'BTCUSD': {
        'price': btc_price,
        'change': btc_change,
        'maw': btc_maw,
        'mam': btc_mam,
        'maa': btc_maa
    },
    'ETHUSD': {
        'price': eth_price,
        'change': eth_change,
            'maw': eth_maw,
        'mam': eth_mam,
        'maa': eth_maa
    }
}

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "a")
f.write("var cr = " + str(crypto) + '\n')
f.close()


# End of file
