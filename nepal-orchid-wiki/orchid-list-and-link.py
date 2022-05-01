#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

website_content = requests.get('https://en.wikipedia.org/wiki/Category:Orchids_of_Nepal').text

soup = BeautifulSoup(website_content, 'lxml')
title = soup.title.string.rstrip()

content = soup.find_all('div', {'class': 'mw-category'})
#print(len(content))

lis = content[0].find_all('li')
#print(len(lis))
for li in lis:
    print(li.a['href'].rstrip())
