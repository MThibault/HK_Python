from collections import namedtuple
import pickle
import os.path

PLAYER_MAX = 5
Player = namedtuple('Player', ['name', 'score'])

def PlayersInit():
    players = []
    for i in range(PLAYER_MAX):
        p = Player(name='', score=0) # initialisation des joueurs au score 0
        players.append(p)
    return players

def update(listPlayers, me):
    ''' 
        listPlayers est la liste des objets Player enregistrée
        me est un joueur, donc un objet de type Player
    '''
    
    for idx, player in enumerate(listPlayers):
        n, s = player.name, player.score
        if me.score > s: # si mon score dépasse l'ancien
            newList = [] # création de la liste updatée
            rightList = listPlayers[idx:]
            del rightList[-1] # suppression du dernier score à droite
            leftList = listPlayers[:idx] # récup des scores avant le score courant
            newList.extend(leftList) # ajout scores avant score courant
            newList.append(me) # ajout score courant
            newList.extend(rightList) # ajout scores après score courant
            listPlayers = newList[:] # copie dans listPlayers
            break # on quitte la boucle
    return listPlayers

def save(path):
    ''' path est le chemin du fichier '''
    with open(path, "wb") as f: # création + ouverture du fichier en mode binaire
        pickle.dump(listPlayers, f, 4) # sauvegarde de l'objet listPlayers dans le fichier f
        
def load(path):
    ''' path est le chemin du fichier '''
    var = None
    if os.path.exists(path): # Si le chemin existe
        try:
            with open(path, 'rb') as f: # on essaye d'ouvrir le fichier
                var = pickle.load(f) # on charge notre liste dans la variable var
        except: pass # Sinon on fait rien, la valeur de var vaut None
    return var

def displayScores():
    pattern = "{name} -> {score}" # format de l'affichage
    for player in listPlayers:
        name, score = player
        if name: # S'il y a un nom 
            print(pattern.format(name=name, score=score)) # on affiche le score

listPlayers = PlayersInit() # Initialisation du tableau de scores

# Ajout des nouveaux scores
# -------------------------
Fred = Player(name='Fred', score=50) # Création d'un joueur + score pour test
Dreamus = Player(name='Dreamus', score=35)
Sakarov  = Player(name='Sakarov', score=40)
listPlayers = update(listPlayers, Fred) # Mise à jour du tableau de scores
listPlayers = update(listPlayers, Dreamus)
listPlayers = update(listPlayers, Sakarov) # on va voir si ça se met bien dans l'ordre décroissant

save("/home/fred1599/Bureau/sauvegarde.txt") # sauvegarde des scores

listPlayers = load("/home/fred1599/Bureau/sauvegarde.txt") # chargement des scores

print(listPlayers) # Affichage de la liste des scores
# [Player(name='Fred', score=50), Player(name='Sakarov', score=40), Player(name='Dreamus', score=35), Player(name='', score=0), Player(name='', score=0)]

displayScores() # bel affichage des scores
# Fred -> 50
# Sakarov -> 40
# Dreamus -> 35