#!/usr/bin/python3.5
from datetime import date

print ("**********Exercice 1**********")
chaine = "Bonjour, je m'appelle"
nom = input ("Entrez votre nom : ")
prenom = input ("Entrez votre prénom : ")
age = input ("Entrez votre age : ")

print ("{} {} {}, j'ai {} ans.". format (chaine, nom, prenom, age))

print ("**********Exercice 2**********")
birth_year = input ("En quelle année es tu né(e) ? : ")
birth_year = int(birth_year)
cur_year = date.today().year
age	= cur_year - birth_year
print ("Vous avez {} ans.". format (age))
