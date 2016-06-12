#!/usr/bin/python3.5

##### Modules #####
import sys
import os.path
from string import punctuation
import re # regular expression

##### Functions ####
def verify_args():
	if (len(sys.argv) != 3):
		sys.exit("Vous devez passer 2 argument au programme, le nom du fichier et le mot à chercher.")

	if (not os.path.exists(sys.argv[1])):
		sys.exit("Le fichier n'existe pas.")

def parse_file(file):
	wordList = []
	with open (file, 'r') as f:
		for line in f:
			wordList += line.split(' ')
	return wordList

def count_searched_words(wordList, wordToFind):
	count = 0
	for word in wordList:
		if word not in punctuation:
			if wordToFind in word:
				count += 1
	return count

##### Implémentations #####
verify_args()
file = sys.argv[1]
wordToFind = sys.argv[2]
count = 0

maListe = parse_file(file)
print(maListe)
count += count_searched_words(maListe, wordToFind)
print (count)