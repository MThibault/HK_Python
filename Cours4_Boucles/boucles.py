#!/usr/bin/python3.5

print("**********Exercice 1**********")
for i in range(11):
	print(i)

print("**********Exercice 2**********")
choix = ""
chaine = ""
while(choix != "."):
	choix = input("Entrez votre mot ou '.' pour terminer la phrase :")
	chaine += choix + " "
print(chaine)

print("**********Exercice 3**********")
mon_tuple = (12, 5, 9, 7, 7)
somme = 0
print(mon_tuple)
for x in mon_tuple:
	somme += x

print(somme)

print("**********Exercice 4**********")
ma_liste = list()
for x in range(10):
	ma_liste.append(int(input("Veuillez rentrer un nombre : ")))

print(ma_liste)
nbr_max = max(ma_liste)
print(nbr_max)
print(ma_liste.index(nbr_max))

print("**********Exercice 5**********")
def fact(n):
	""" fact(n) : Calcul la factorielle de n (entier >= 0) """
	if n < 2:
		return 1
	else:
		return n*fact(n - 1)

print(fact(int(input("Veuillez rentrer un nombre : "))))

print("**********Exercice 6**********")
nbr = int(input("Veuillez choisir un nombre : "))
for i in range(1,11):
	print("{} * {} = {}". format(nbr, i, nbr*i))

print("**********Exercice 7**********")
ma_liste = list()
nbr = int(input("Veuillez rentrer un nombre : "))
for i in range(nbr):
	ma_liste.append(0)

print(ma_liste)

print("**********Exercice 8**********")
limite = int(input("Veuillez choisir combien de nombre vous souhaitez entrer : "))
ma_liste = list()
nb_neg = 0
nb_pos = 0
for i in range(limite):
	ma_liste.append(int(input("Entrez un nombre : ")))
	if (ma_liste[i] < 0):
		nb_neg += 1
	else:
		nb_pos += 1

print("Nombre de nombre négatif : {}".format (nb_neg))
print("Nombre de nombre positif : {}".format (nb_pos))

print("**********Exercice 9**********")
def rempliList(liste):
	for i in range(4):
		liste.append(int(input("Veuillez rentrer un nombre : ")))

	return liste

ma_liste = list()
ma_liste1 = list()
ma_liste2 = list()

ma_liste1 = rempliList(ma_liste1)
print(ma_liste1)
ma_liste2 = rempliList(ma_liste2)
print(ma_liste2)

for x in range(4):
	ma_liste.append(ma_liste1[x] + ma_liste2[x])

print(ma_liste)

print("**********Exercice 10**********")
schtroumpf = 0
for x in range(4):
	for y in range(4):
		schtroumpf += int(ma_liste1[x] * ma_liste2[y])
print(schtroumpf)