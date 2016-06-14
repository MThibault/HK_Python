#!/usr/bin/python3.5

def div(a, b, default=0):
	try:
		return a/b
	except (ZeroDivisionError, TypeError):
		return default

# Lever sa propre expression
def div(a, b):
	if b == 0:
		raise Exception("Entrer un nombre différent de 0")