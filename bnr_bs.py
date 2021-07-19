import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
link = BeautifulSoup(r.text, "html.parser")
title = link.find_all('div', attrs={'class': 'contentDiv'})
for i in title:
    for tr_index in i.find_all("table")
        print(tr_index)
