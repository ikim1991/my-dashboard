# ETL Pipeline to retrieve the exchange rate data of USD and CAD from Yahoo Finance using web scraping

# Libraries used in ETL
import requests
import bs4
from bs4 import BeautifulSoup

# API Request from Yahoo Finance
r = requests.get('https://ca.finance.yahoo.com/quote/CADUSD=X?p=CADUSD=X')

# Web Scrap into HTML format using BeautifulSoup library
soup = bs4.BeautifulSoup(r.text, "html.parser")
container = soup.findAll('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})

# Get quote and change for USD/CAD exchange rate and load in a Python Dictionary
currency = {
    'USDCAD':{
        'price': container[0].div.span.text,
        'change': container[0].div.div.span.text
    }
}

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "a")
f.write("var currency = " + str(currency) + '\n')
f.close()

# End of file
