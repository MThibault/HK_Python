#!/usr/bin/python3.5

##### Modules #####
import sys
import os.path

##### Implementation #####
print(len(sys.argv))
if os.path.exists('score.txt'):
	print("Le fichier existe!\n")