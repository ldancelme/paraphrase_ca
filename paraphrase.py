#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: lLOX
"""
import spacy
from spacy import displacy
import requests
from bs4 import BeautifulSoup
import random

# =======================================================
#                Sentence Analysis
# =======================================================
nlp = spacy.load("fr_core_news_sm")

#sentence = 'Mais, vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres, des gens qui m’ont tendu la main, peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi. Et c’est assez curieux de se dire que les hasards, les rencontres forgent une destinée… Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l’interlocuteur en face, je dirais, le miroir qui vous aide à avancer. Alors ce n’est pas mon cas, comme je le disais là, puisque moi au contraire, j’ai pu ; et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie… Je ne suis qu’amour ! Et finalement, quand beaucoup de gens aujourd’hui me disent : « Mais comment fais-tu pour avoir cette humanité ? » Eh bien je leur réponds très simplement, je leur dis que c’est ce goût de l’amour, ce goût donc qui m’a poussé aujourd’hui à entreprendre une construction mécanique, mais demain, qui sait, peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi...'
sentence = input()
doc = nlp(sentence)

    
# Text Preprocessing | Lemmatization
print("\n" + f"Token\t\tLemma\t\tStopword\tDEP\t\tPOS".format('Token', 'Lemma', 'Stopword'))
print("-"*70)
for token in doc:
    print(f"{str(token)}\t\t{token.lemma_}\t\t{token.is_stop}\t\t{token.dep_}\t\t{token.pos_}")

pos_tochange = ['PRON', 'VERB', 'NOUN','ADJ']    
sentence_dict = {idx:str(token) for (idx,token) in enumerate(doc)}
to_synos = {idx:str(token) for (idx,token) in enumerate(doc) if token.pos_ in pos_tochange}

# =======================================================
#                   Web Scrapping
# =======================================================
def extract_synos(word):
    
    url = 'http://www.synonymo.fr/syno/' + str(word)
    get = requests.get(url)
    get.encoding = get.apparent_encoding
    html = get.text
    
    soup = BeautifulSoup(html, features='lxml')
    raw_text = soup.prettify()
    
    ul = soup.find('ul', {'class':'synos'})
    
    try : 
        first = ul.findAll('a')
        synos = [i.next for i in first]
#        print('\nSynonyms of {} :'.format(word))
#        print(synos)
        
    
        syno = random.choice(synos)
        return syno
    
    except AttributeError:
#        raise Exception('Your word ({}) is not in synonymo.fr'.format(word))
        return word    
    
    

# =======================================================
#                Sentence Generation
# =======================================================
synos = [extract_synos(x) for x in to_synos.values()]
synos_dict = {}
for idx, val in zip(to_synos.keys(), synos):
    d = {idx: val}
    synos_dict.update(d)


    
print("\n" + f"IDX\tWORD\t\tSYNONYM")
print("-"*34)
for i, w, s in zip(to_synos.keys(), to_synos.values(), synos):
    print(f"{i}\t{w}\t\t{s}")
    
paraphrase_dict = sentence_dict.copy()
for i in synos_dict.keys():
    paraphrase_dict[i] = synos_dict[i] 

new_sentence = " ".join(paraphrase_dict.values())
print('\n\n"{}" devient "{}"'.format(sentence, new_sentence))
    
#displacy.render(doc, style="ent")