# -*- coding: utf-8 -*-
"""
Author : LOX

"""

import requests
from bs4 import BeautifulSoup
import urlencode
word = 'bite'
url = 'http://www.synonymo.fr/syno/' + word
get = requests.get(url)
html = get.text



soup = BeautifulSoup(html)
raw_text = soup.prettify()

ul = soup.find('ul', {'class':'synos'})

first = ul.findAll('a')
synos = []
for i in first:
    synos.append(i.next)

# # Write synonyms to a new file
# file = word + '.txt'
# out = open(file , 'a')
# out.write(raw_text)
# out.close()