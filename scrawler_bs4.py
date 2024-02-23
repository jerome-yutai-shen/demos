# -*- coding: utf-8 -*-
"""
Created on Feb 23 10:36:37 2024

@author: Jerome Yutai Shen

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data = []

data_iterator = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text
        data.append((country, confirmed, deaths, continent))

    except StopIteration:
        break
# Sort the data by the number of confirmed cases
data.sort(key = lambda row: row[1], reverse = True)
df = pd.DataFrame(data, columns = ['Country', 'Confirmed','Deaths','Continent'])
print(df.head(100))