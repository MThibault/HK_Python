#!/usr/bin/python3.5

print("**********Exercice 1**********")
ma_liste = [1, 2, 3]
print(ma_liste)
ma_liste.remove(1)
ma_liste.append(3)
print(ma_liste)

print("**********Exercice 2**********")
mon_dico = {"AS": 11, "10": 10, "ROI": 4, "DAME": 3}
print(mon_dico)

print("**********Exercice 3**********")
mon_tuple = (1, 2, 3)
ma_liste = list(mon_tuple)
print(ma_liste)
ma_liste.remove(1)
ma_liste.append(3)
mon_tuple = ma_liste
print(mon_tuple)