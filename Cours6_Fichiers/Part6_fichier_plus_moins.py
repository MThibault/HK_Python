#!/usr/bin/python3.4

##### Modules #####
import os
from random import randrange

def plusMoins(nbr, choix):
	if(choix > nbr):
		print("C'est moins.")
	else:
		print("C'est plus.")

def writeInFile(mon_tuple, file):
	with open(file, 'a') as f:
		f.write('{};{};{}'.format(mon_tuple[0], mon_tuple[1], mon_tuple[2]))

nombreAleatoire = randrange(1, 1000)
choix = 0
count = 0

while choix != nombreAleatoire:
	choix = int(input("Entrez un nombre entre 1 et 1000 : "))
	plusMoins(nombreAleatoire, choix)
	count += 1

print("Bravo, trouvé en {} coups!".format(count))
firstname = input("Quel est ton prénom : ")
lastname = input("Quel est ton nom : ")
lastname += '\n'
with open('score.txt', 'r') as f:
	is_done = False
	for line in f:
		mon_tuple = ()
		mon_tuple = line.split(';') # Récupération de chaque ligne
		if(int(mon_tuple[0]) > count and is_done == False):
			writeInFile((count, firstname, lastname), 'tmp.txt')
			writeInFile(mon_tuple, 'tmp.txt')
			is_done = True
		else:
			writeInFile(mon_tuple, 'tmp.txt')
	
	if is_done != True:
		writeInFile((count, firstname, lastname), 'tmp.txt')

os.rename('tmp.txt', 'score.txt')

with open('score.txt', 'r') as f:
	for line in f:
		print(line)