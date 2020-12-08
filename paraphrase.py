#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: LOX
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
#sentence = "puceau moi ? serieusement ^^ haha on me l avait pas sortie celle la depuis loooongtemps 🙂 demande a mes potes si je suis puceau tu vas voir les reponses que tu vas te prendre XD rien que la semaine passee j ai niquer donc chuuuuut ferme la puceau de merde car oui toi tu m as tout l air d un bon puceau de merde car souvent vous etes frustrer de ne pas BAISER 🙂 ses agreable de se faire un missionnaire ou un amazone avec une meuf hein? tu peux pas repondre car tu ne sais pas ce que c ou alors tu le sais mais tu as du taper dans ta barre de recherche 'missionnaire sexe' ou 'amazone sexe' pour comprendre ce que c etait mdddrrr !! c est grave quoiquil en soit.... pour revenir a moi, je pense que je suis le mec le moins puceau de ma bande de 11 meilleurs amis pas psk j ai eu le plus de rapport intime mais psk j ai eu les plus jolie femme que mes amis :) ses pas moi qui le dit, ses eux qui commente sous mes photos insta 'trop belle la fille que tu as coucher avec hier en boite notamment!' donc apres si tu veux que sa parte plus loi sa peut partir vraiment loi j habite dans la banlieue de niort sa te parle steven sanchez ? ses juste un cousin donc OKLM hahaha on verra si tu parles encore le puceau de merde mdddrrr pk insulter qd on est soi meme puceau tu me feras toujour marrer!"
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
print('\n\n"{}"\n\ndevient\n\n"{}"'.format(sentence, new_sentence))
    
#displacy.render(doc, style="ent")