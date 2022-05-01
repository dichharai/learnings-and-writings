#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

file = open('nepal-orchid-list-link.txt', 'r')
links = file.readlines()

# link_0 = links[0].rstrip()
# print(link_0)

for link in links: 
    website_content = requests.get('https://en.wikipedia.org'+link.rstrip()).text
    soup = BeautifulSoup(website_content, 'lxml')
    title = soup.find('h1', {'id': 'firstHeading'}).string.rstrip()
    pat = '='*len(title)
    print(title)
    print(pat)

    #content = soup.find('div', {'class': 'mw-parser-output'})
    content = soup.find_all('p')
    # print(len(content))
    # print(content[1].getText())
    descrip = content[1].getText()
    #descrip = descrip[0: descrip.index('[')] + descrip[descrip.index('3]')+3: len(descrip)]

    print(descrip)

    tbody = soup.find_all('tbody')
    #print(len(tbody))
    trs = tbody[0].find_all('tr')
    image_link = trs[1]
    if image_link.find('td'):
        print(image_link.td.a['href'])

file.close()
