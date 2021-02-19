from bs4 import BeautifulSoup
from scipy import stats
import numpy as np
import requests
import pprint
import pandas as pd
import csv
import itertools

item_name = []
prices = []

for i in range(1, 10):
    ebayUrl = "https://www.ebay.fr/b/Apple/bn_7064582728?_pgn=" + str(i)
    print(ebayUrl)

    r = requests.get(ebayUrl)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    prices = soup.find_all('span', attrs={'class': 's-item__price'})
    item_name = soup.find_all('span', attrs={'class': 's-item__title'})

print(prices)
print(item_name)
