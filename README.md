# *Paraphrase_ca* 
Application Python dont le but est d'extraire les noms, adverbe, adjectifs etc. d'une phrase et de les remplacer par leur synonyme.

## 1ère Stratégie
- Analyse en *POS tagging* (Part-of-Speech tagging) de la phrase à l'aide de la librairie SpaCy afin de reconnaître et extraire les mots à remplacer dans la phrase.
- *Web Scrapping* à partir des sites "Dictionnaire de Synonymes" français disponible (ex: [Synonymo.fr](https://synonymo.fr/)).
- Choix au hasard dans les listes de synonymes extraites et reconstitution de la phrase.

### Binder link to preview *paraphrase_ca* notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ldancelme/paraphrase_ca/HEAD)
