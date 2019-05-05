# ETL Pipeline to retrieve the price of crude oil from Yahoo Finance using web scrap

# Libraries used in ETL
import datetime
import requests
import bs4
from bs4 import BeautifulSoup

# Sets todays/last years date using datetime
day = datetime.datetime.now().day
month = datetime.datetime.now().month
year = datetime.datetime.now().year
last_year = year - 1

# Format datetimes for URL query parameters
start = datetime.datetime(last_year, month, day).strftime('%b-%d-%Y')
end = datetime.datetime.now().strftime('%b-%d')

# API Request from Yahoo Finance
r = requests.get('https://www.redflagdeals.com/flyers/metro/weekly-{}-to-{}-134720/'.format(end, start))

# Web Scrap into HTML format using BeautifulSoup library
soup = bs4.BeautifulSoup(r.text, "html.parser")
container = soup.findAll('li',{'class': 'flyer_product_info rfd_modal'})

# Initialize our datasets
name = []
price = []

# Predefined keywords to look for depending on the user's preferences
keywords = ['steak', 'beef', 'eggs', 'milk', 'chicken', 'pasta', 'salmon', 'juice', 'bread']

# Only retrieves products that is included in our list of keywords
for product in container:
    for k in keywords:
        if k in product.p.text.lower():
            name.append(product.p.text)
            price.append(product.li.p.text)
        else:
            continue

# Initialize our dataset into a Python Dictionary
deals = {}

# Load our data into ditionary
for i in range(len(name)):
    deals[name[i]] = price[i]

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "a")
f.write("var deals = " + str(deals) + '\n')
f.close()
