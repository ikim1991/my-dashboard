# ETL Pipeline to retrieve the price of crude oil from Yahoo Finance using web scrap

# Libraries used in ETL
import requests
import bs4
from bs4 import BeautifulSoup

# API Request from Yahoo Finance
r = requests.get('https://ca.finance.yahoo.com/quote/CL=F?p=CL=F')

# Web Scrap into HTML format using BeautifulSoup library
soup = bs4.BeautifulSoup(r.text, "html.parser")
container = soup.findAll('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})

# Get crude oil price and change and load in a Python Dictionary
commodity = {
    'Crude':{
        'price': container[0].div.span.text,
        'change': container[0].div.div.span.text
    }
}

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "w")
f.write("var commodity = " + str(commodity) + '\n')
f.close()

# End of File
