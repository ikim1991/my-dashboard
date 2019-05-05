# ETL Pipeline for extracting stocks and financial data using yahoo finance API in pandas datareader

# Libraries used in ETL
import pandas as pd
from pandas_datareader import data as web
import datetime

# Sets todays/last years date using datetime
day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year
last_year = year - 1

# Todays date
start = datetime.datetime(last_year, month, day).strftime('%Y-%m-%d')
# Last year from todays date
end = datetime.datetime.now().strftime('%Y-%m-%d')

# Set tickers of the stocks/indices we want to extract
tickers = ['^GSPTSE', '^GSPC', 'FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']

# Creates a Pandas dateframe for data wrangling
data = pd.DataFrame()

# Loops through each of our tickers and extracts the closing prices of each into our dataframe
for t in tickers:
    data[t] = web.DataReader(t, 'yahoo', start, end)['Adj Close']

# Fill any missing data in our dataframe, which may be caused by the different exchanges the stocks trade on
data.fillna(method = "ffill", inplace=True)

# Sets n to always retrieve the row of our most recent data
n = len(data) - 1

# Extracts the close price, change in price, weekly, monthly, and yearly moving averages of data from the most present date
price = data.iloc[n]
change = (data.iloc[n] - data.iloc[n-1]) / (0.01 * data.iloc[n])
maw = data.rolling(7).mean().iloc[n]
mam = data.rolling(30).mean().iloc[n]
maa = data.rolling(n).mean().iloc[n]

# Transform our data into a Python dictionary datatype
stocks = {}
for t in tickers:
    stocks[t] = {'price': price[t],
                    'change': change[t],
                    'maw': maw[t],
                    'mam': mam[t],
                    'maa': maa[t]
                   }
# A function to loop through our data in our dictionary and round our values to 2 significant figures
def round_values(df):
    for t in tickers:
        keys = df[t].keys()
        for k in keys:
            df[t][k] = round(df[t][k], 2)

    return df

# Call our round_values function on our dictionary
round_values(stocks)

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "a")
f.write("var stocks = " + str(stocks) + '\n')
f.close()

# End of file
