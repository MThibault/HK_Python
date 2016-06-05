#!/usr/bin/python3.5

print("**********Exercice 1**********")
def pgcd(a, b):
	while a != b:
		if a > b:
			a -= b
		elif a < b:
			b -= a
	return a

a = 56
b = 42

print("Le PGCD est {}.". format(pgcd(a, b)))

print("**********Exercice 2**********")
def reverse_string(str1):
	result = ""	
	for lettre in str1:
		result = lettre + result

	return result

def is_anagram(str1, str2):
	if (len(str1) == len(str2)):
		for i in range(len(str1)):
			if str1[i] != str2[i]:
				return False

		return True
	else:
		return False

str1 = "Kayak".lower()
str2 = "KaYaK".lower()

print("Chaine 1 : {}, chaine 2 : {}, anagramme : {}.". format(str1, str2, is_anagram(str1, reverse_string(str2))))

print("**********Exercice 3**********")
def crypt(string_1):
	decalage = 2
	newWord = ""

	for lettre in string_1:
		newWord += chr(ord(lettre) + decalage)

	return newWord

plainText = input("Veuillez entrer une phrase : ")
print("Crypt : {}". format(crypt(plainText)))