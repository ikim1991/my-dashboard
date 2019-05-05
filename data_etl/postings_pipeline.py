# ETL Pipeline to retrieve data science related job postings on indeed.com using web scraping

# Libraries used in ETL
import requests
import bs4
from bs4 import BeautifulSoup

# API Request from indeed.com
r = requests.get('https://ca.indeed.com/jobs?as_and=data+scientist&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=10&l=Toronto%2C+ON&fromage=any&limit=50&sort=date&psf=advsrch')

# Web Scrap into HTML format using BeautifulSoup library
soup = bs4.BeautifulSoup(r.text, "html.parser")

# Retrieves basic posting information
title = soup.findAll('div', {'class': 'title'})
company = soup.findAll('span', {'class': 'company'})

# Initialize our Python dictionary dataset
data = {}

# Load our results into our dataset
for i in range(len(title)):
    data[i] = {
        'title': title[i].text.strip(),
        'company': company[i].text.strip(),
        'link': 'https://indeed.com/'+title[i].a['href']
    }

# Filter our data to only show results with the keyword 'data', 'analy', and 'developer'
for i in range(len(data)):
    if ('data' in data[i]['title'].lower()) | ('analy' in data[i]['title'].lower()) | ('developer' in data[i]['title'].lower()):
        continue
    else:
        del data[i]

# Load data into a Javascript file as an Object Datatype/JSON format
f = open("./data/data.js", "a")
f.write("var postings = " + str(data) + '\n')
f.close()

# End of File
