#!/usr/bin/python3.5

##### Classes #####
class Chaise:
	# Constructeur
	def __init__(self, nom, couleur, poids):
		self.nom = nom
		self.couleur = couleur
		self.poids = poids

	def modifier(self, couleur):
		self.couleur = couleur

##### Implémentations #####
regence = Chaise('régence', 'brun', 6)

print(regence.nom)
print(regence.couleur)
print(regence.poids)

regence.modifier('blanc')
print(regence.couleur)