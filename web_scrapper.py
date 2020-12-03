# -*- coding: utf-8 -*-
"""
@author : LOX
"""

import requests
from bs4 import BeautifulSoup

word = input()
url = 'http://www.synonymo.fr/syno/' + word
get = requests.get(url)
get.encoding = get.apparent_encoding
html = get.text



soup = BeautifulSoup(html, features='lxml')
raw_text = soup.prettify()

ul = soup.find('ul', {'class':'synos'})

first = ul.findAll('a')
synos = []
for i in first:
    synos.append(i.next)


print('\nSynonyms of {} :'.format(word))
for s in synos:
    print(s)

# # Write synonyms to a new file
# file = word + '.txt'
# out = open(file , 'a')
# out.write(raw_text)
# out.close()