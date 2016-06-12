#!/usr/bin/python3.5

##### Modules #####
import sys
import os.path
from string import punctuation

##### Functions ####
def verify_args():
	if (len(sys.argv) != 2):
		sys.exit("Vous devez passer 1 argument au programme, le nom du fichier.")

	if (not os.path.exists(sys.argv[1])):
		sys.exit("Le fichier n'existe pas.")

def parse_file(file):
	wordList = []
	with open (file, 'r') as f:
		for line in f:
			wordList += line.split(' ')
	return wordList

def count_words(wordList):
	count = 0
	for word in wordList:
		if word not in punctuation:
			count += 1
	return count

##### Implémentations #####
verify_args()
file = sys.argv[1]
count = 0

maListe = parse_file(file)
print(maListe)
count += count_words(maListe)
print (count)