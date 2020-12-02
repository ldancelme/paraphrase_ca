# -*- coding: utf-8 -*-
"""
Author : LOX

"""

import requests
import os 

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
word = 'bite'
url = 'http://www.synonymo.fr/syno/' + word
r = requests.get(url)
raw_text = r.text

raw_text = str(raw_text)
# Write synonyms to a new file
file = word + '.txt'
out = open(file , 'a')
out.write(raw_text)
out.close()