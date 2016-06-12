#!/usr/bin/python3.4

##### Modules #####
import os

##### Functions #####
def add():
	lastname = input("Donner le nom : ")
	firstname = input("Donner le prénom : ")
	address = input("Donner l'adresse : ")
	phone = input("Donner le numéro de téléphone : ")
	phone += '\n'
	return (lastname, firstname, address, phone)

def remove():
	mon_tuple = ()
	readFile()
	lastname = input("Entrer le nom de la personne à supprimer : ")
	firstname = input("Entrer le prenom de la personne à supprimer : ")
	with open(carnet, 'r') as f:
		for line in f:
			mon_tuple = line.split(';') # Récupération de chaque ligne
			if(not (lastname == mon_tuple[0] and firstname == mon_tuple[1])): # Si c'est la ligne à modifier
				writeInFile(mon_tuple, tmp_file)
	os.rename(tmp_file, carnet)

def modify():
	mon_tuple = ()
	readFile()
	lastname = input("Entrer le nom de la personne à modifier : ")
	firstname = input("Entrer le prenom de la personne à modifier : ")
	with open(carnet, 'r') as f:
		for line in f:
			mon_tuple = line.split(';') # Récupération de chaque ligne
			if(lastname == mon_tuple[0] and firstname == mon_tuple[1]): # Si c'est la ligne à modifier
				print('Entrer les nouvelles informations :')
				writeInFile(add(), tmp_file) # On enregistre la ligne modifiée
			else:
				writeInFile(mon_tuple, tmp_file) # On recopie la ligne
	os.rename(tmp_file, carnet)

def menu():
	return input("\n1 - Ajouter une adresse\n"
					"2 - Modifier une adresse\n"
					"3 - Effacer une adresse\n"
					"Votre choix ? ")

def readFile():
	with open('Carnet.txt', 'r') as f:
		for line in f:
			print(line)	

def writeInFile(mon_tuple, file):
	with open(file, 'a') as f:
		f.write('{};{};{};{}'.format(mon_tuple[0], mon_tuple[1], mon_tuple[2], mon_tuple[3]))

tmp_file = 'tmp.txt'
carnet = 'Carnet.txt'

##### Implementation #####
choix = menu()
print(choix)

if choix == '1':
	writeInFile(add(), carnet)
elif choix == '2':
	modify()
elif choix == '3':
	remove()
else:
	print("Choix non proposé.")