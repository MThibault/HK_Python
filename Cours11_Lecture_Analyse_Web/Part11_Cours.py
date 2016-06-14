#!/usr/bin/python3.5

##### Modules #####
from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from lxml import html # Classe html pour travailler avec du HTML

# URL dont tout va partir, on ajoutera nos urls de MP3 à celle-ci
BASE_URL = "http://hcmaslov.d-real.sci-nnov.ru/public/mp3/Beatles/02%20With%20The%20Beatles/"

# urlopen pour ouvrir la page, et read pour avoir le résultat sous forme de chaines de caractères
data = urlopen(BASE_URL).read()

tree = html.fromstring(data) # Pour rendre le code HTML propre

# './/a[contains(text(), "mp3")]/@href'
# //x -> recherche à la racine la balise x
# /x -> recherche la balise suivante x
# @x -> recherche toutes les valeurs de la propriété x
elements = tree.xpath('.//a[contains(text(), "mp3")]/@href')
for count, href in enumerate(elements):
	# Joindre mes URLs
	url = urljoin(BASE_URL, href)
	titre = href.replace("%20", " ")
	print("url n°{}: {}".format(count+1, titre))
	# télécharger le MP3
	urlretrieve(url, "/home/thibault/Musique/{}".format(titre))