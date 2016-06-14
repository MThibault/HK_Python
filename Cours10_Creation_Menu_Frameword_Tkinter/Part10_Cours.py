from tkinter import filedialog
import tkinter as tk
import os

# Les différentes actions à executer

def fopen():
	currentPath = os.getcwd() # Chemin courant
	myFile = filedialog.askopenfile\
	(
		mode='r', 
		defaultextension='.txt', 
		initialdir=currentPath
	) # Ouverture de la fenêtre pour choisir le fichier
	content = myFile.read() # Texte du fichier ouvert
	text.insert(tk.END, content) # Insertion du texte dans le widget Text

def save():
	''' à compléter '''
	pass
# ----------------------------------------------------------

# Programme principal

# ----------------------------------------------------------

# Créer la fenêtre parente

root = tk.Tk()

# Création d'une fenêtre text pour ajouter le texte d'un fichier ouvert (pour l'exemple)

text = tk.Text(root)
text.pack()

# Créer sa barre de menu dans la fenêtre parente

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
editmenu = tk.Menu(menubar, tearoff=0)

# Ajouter les différentes options dans la barre de menu

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)

# Ajouter les différentes actions pour chaque option

filemenu.add_command(label='Ouvrir', command=fopen)
filemenu.add_command(label='Sauvegarder', command=save)
filemenu.add_command(label='Quitter', command=root.quit) # quitte le programme

# Lancement de la boucle événementielle

root.config(menu=menubar)
root.mainloop()