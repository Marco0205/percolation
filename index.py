# Dans les fonctions suivantes : 0 = noir et 1 = jaune
# Entree pour savoir la case dans laquelle on se trouve : ordonnee(entre 0 et n-1), abscisse(entre 0 et n-1)
# Fonction qui génere des listes de listes aléatoires
from random import randint

def generer_grille(n):
    """
    Fonction qui créé des listes de listes de taille n * n
    Entree : un entier n qui définit le taille des listes
    Sortie : Une liste de liste de taille n * n contenant des 0 et des 1
    """
    liste_finale = []
    for i in range (n):
        liste_finale.append([])
    for liste in liste_finale:
        for i in range(n):
            tmp = randint(0, 1)
            liste.append(tmp)
    return liste_finale

# Fonctions qui déterminent la couleur de certaines cases

ordonnee = 0
abscisse = 0
grille = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0]]

# Fonction qui détermine la couleur d'une case donnee

def trouver_couleur_case(ordonnee, abscisse, grille):
    """
    Fonction qui détermine la couleur d'une case donnee
    Entree : la rangee d'une case donnée, le numero de cette case dans cette rangee, la grille de base
    Sortie : La couleur de la case donnée
    """
    bit_case = grille[ordonnee][abscisse]
    return(bit_case)

assert(trouver_couleur_case(2, 4, grille) == 1)
assert(trouver_couleur_case(0, 0, grille) == 0)

# Fonction qui determine la couleur de la case a droite d'une case choisie

def couleur_case_droite(ordonnee, abscisse, grille):
    """
    Fonction qui détermine la couleur de la case a droite d'une case donnée
    Entree : la rangee d'une case donnée, le numero de cette case dans cette rangee, la grille de base
    Sortie : La couleur de la case a droite de la case donnée en entrée
    """
    if abscisse == (len(grille[ordonnee])-1): # on met le -1 car pour la ligne suivante, on compte de 0 a 9 et non de 1 a 10
        return(None)
    else:
        bit_case_droite = grille[ordonnee][abscisse + 1] # abs + 1 car on veut la case de droite
        return(bit_case_droite)

assert(couleur_case_droite(0, 0, grille) == 0)
assert(couleur_case_droite(5, 9, grille) == None)
assert(couleur_case_droite(2, 6, grille) == 0)

# Fonction qui determine la couleur de la case a gauche d'une case choisie

def couleur_case_gauche(ordonnee, abscisse, grille):
    """
    Fonction qui détermine la couleur de la case a gauche d'une case donnée
    Entree : la rangee d'une case donnée, le numero de cette case dans cette rangee, la grille de base
    Sortie : La couleur de la case a gauche de la case donnée en entrée
    """
    if abscisse == 0: # car si abs = 0, alors il n'y a pas de case a gauche
        return(None)
    else:
        bit_case_gauche = grille[ordonnee][abscisse - 1] # abs - 1 car on veut la case de gauche
        return(bit_case_gauche)

assert(couleur_case_gauche(0, 1, grille) == 0)
assert(couleur_case_gauche(7, 0, grille) == None)
assert(couleur_case_gauche(4, 3, grille) == 1)

# Fonction qui détermine la couleur de la case d'au dessus

def couleur_case_dessus(ordonnee, abscisse, grille):
    """
    Fonction qui détermine la couleur de la case du dessus
    Entree : la rangee d'une case donnée, le numero de cette case dans cette rangee, la grille de base
    Sortie : La couleur de la case au dessus de la case donnée en entrée
    """
    if ordonnee == 0:
        return(None)
    else:
        bit_case_dessus = grille[ordonnee - 1][abscisse]
        return(bit_case_dessus)

assert(couleur_case_dessus(0, 2, grille) == None)
assert(couleur_case_dessus(9, 2, grille) == 0)
assert(couleur_case_dessus(1, 2, grille) == 0)

# Fonction qui determine la couleur de la case d'en dessous

def couleur_case_dessous(ordonnee, abscisse, grille):
    """
    Fonction qui détermine la couleur de la case du dessous
    Entree : la rangee d'une case donnée, le numero de cette case dans cette rangee, la grille de base
    Sortie : La couleur de la case en dessous de la case donnée en entrée
    """
    if ordonnee == len(grille) - 1:
        return(None)
    else:
        bit_case_dessous = grille[ordonnee + 1][abscisse]
        return(bit_case_dessous)

assert(couleur_case_dessous(0, 0, grille) == 0)
assert(couleur_case_dessous(9, 0, grille) == None)
assert(couleur_case_dessous(7, 0, grille) == 0)
assert(couleur_case_dessous(2, 5, grille) == 1)

# Fonction qui colorie la ligne 1 en bleu

def colorier_ligne1(grille):
    """
    Cette fonction colorie les cases jaunes de la premiere ligne d'une grille en bleu
    Entree : grille
    Sortie : la grille avec la premiere ligne modifiee
    """
    for i in range(len(grille[0])):
        couleur_case = trouver_couleur_case(0, i, grille)
        if couleur_case == 1:
            grille[0][i] = 2
    return(grille)

assert(colorier_ligne1(grille) == [[0, 0, 0, 0, 2, 2, 2, 2, 0, 2], [0, 0, 1, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0]])

# Algorithme d'écoulement

# Grille de tests
grille1 = [[0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 0, 0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1, 0, 0]]

# Fonction

def ecoulement(grille, taille_liste):
    """
    Fonction qui fait le calcul pour l'écoulement du liquide dans la grille
    Entree : Grille de départ, taille d'une liste de la grille
    Sortie : la grille avec les bonnes cases coloriees
    """
    grille = colorier_ligne1(grille)
    for k in range(taille_liste-1):
        for i in range(taille_liste):
            if trouver_couleur_case(k, i, grille) == 2 and couleur_case_dessous(k, i, grille) == 1:
                grille[k+1][i] = 2
        for i in range(taille_liste):
            if trouver_couleur_case(k+1, i, grille) == 2 and couleur_case_droite(k+1, i, grille) == 1:
                grille[k+1][i+1] = 2
        for i in range(taille_liste-1,-1 , -1):
            if trouver_couleur_case(k+1, i, grille) == 2 and couleur_case_gauche(k+1, i, grille) == 1:
                grille[k+1][i-1] = 2
    return(grille)

def ecoulement_version2(grille, taille_liste):
    """
    Fonction qui fait le calcul pour l'écoulement du liquide dans la grille et qui prend en compte la remontee de l'eau
    Entree : Grille de départ, taille d'une liste de la grille
    Sortie : la grille avec les bonnes cases coloriees
    """
    grille = colorier_ligne1(grille)
    for k in range(taille_liste-1):
        for i in range(taille_liste):
            if trouver_couleur_case(k, i, grille) == 2 and couleur_case_dessous(k, i, grille) == 1:
                grille[k+1][i] = 2
        for i in range(taille_liste):
            if trouver_couleur_case(k+1, i, grille) == 2 and couleur_case_droite(k+1, i, grille) == 1:
                grille[k+1][i+1] = 2
        for i in range(taille_liste-1, -1, -1):
            if trouver_couleur_case(k+1, i, grille) == 2 and couleur_case_gauche(k+1, i, grille) == 1:
                grille[k+1][i-1] = 2
    for k in range(taille_liste-1, -1, -1):
        for i in range(taille_liste):
            if trouver_couleur_case(k, i, grille) == 2 and couleur_case_dessus(k, i, grille) == 1:
                grille[k-1][i] = 2
        for i in range(taille_liste):
            if trouver_couleur_case(k-1, i, grille) == 2 and couleur_case_droite(k-1, i, grille) == 1:
                grille[k-1][i+1] = 2
        for i in range(taille_liste-1, -1, -1):
            if trouver_couleur_case(k-1, i, grille) == 2 and couleur_case_gauche(k-1, i, grille) == 1:
                grille[k-1][i-1] = 2
    return(grille)


# Partie Graphique

from matplotlib import *
import pyxel
def affichage(grille):
    """
    Fonction qui permet d'afficher la grille de taille Lxl grace au tableau généré auparavant
    Entree : la grille de départ
    Sortie : la grille de façon graphique
    """
    # color = 10
    # nb_c_l = input("Nombre de colonnes et lignes: ")
    L = L2*10
    l = L2*10
    pyxel.init(L, l)
    def update():
        nonlocal grille #grille = generer_grille(10)
        taille_liste = len(grille)
        if pyxel.btnp(pyxel.KEY_U):
            grille = ecoulement_version2(grille, taille_liste)
        draw()
    def draw():
        pos_x = -(L/L2)+1
        pos_y = 1
        pyxel.cls(7)
        color = 10
        for u in range(0,len(grille)):
            for i in range(0,len(grille)):
                if grille[u][i] == 0:
                    color = 0
                elif grille[u][i] == 1:
                    color = 10
                else:
                    color = 5
                pos_x += L/L2
                if pos_x == L+1:
                    pos_y +=l/L2
                    pos_x = 1
                    pyxel.rect(pos_x, pos_y, L/L2-0.5, l/L2-0.5, color)
                else:
                    pyxel.rect(pos_x, pos_y, L/L2-0.5, l/L2-0.5, color)
    pyxel.run(update, draw)


# print(affichage(grille1))

def affichage_version2(grille):
    """
    Fonction qui permet d'afficher la grille de taille Lxl grace au tableau généré auparavant
    Entree : la grille de départ
    Sortie : la grille de façon graphique
    """
    L = L2*10
    l = L2*10
    pos_x = -(L/L2)+1
    pos_y = 1

    pyxel.init(L, l)
    pyxel.cls(7)
    # pyxel.rect(1, 10, L/10-1, l/10-1, 5)
    color = 10
    for u in range(0,len(grille)):
        for i in range(0,len(grille)):
            if grille[u][i] == 0:
                color = 0
            elif grille[u][i] == 1:
                color = 10
            else:
                color = 5
            pos_x += L/L2
            if pos_x == L+1:
                pos_y +=l/L2
                pos_x = 1
                pyxel.rect(pos_x, pos_y, L/L2-0.5, l/L2-0.5, color)
            else:
                pyxel.rect(pos_x, pos_y, L/L2-0.5, l/L2-0.5, color)
    pyxel.show()

# Fonction qui demande a l'utilisateur quelle grille il veut afficher
L2 = int(input("largeur/Largeur de la grille: "))

def choix_utilisateur(grille):
    """
    Fonction qui demande a l'utilisateur quelle grille il veut afficher entre la pleine et la vide
    Entree : grille de base non travaillee
    """
    choix = int(input("Inserez 1 pour voir la grille de départ. Inserez 2 pour voir la grille pleine."))
    if choix == 1:
        print(affichage_version2(grille))
    else:
        print(affichage_version2(ecoulement(grille, len(grille))))


grille_finale = generer_grille(L2)
choix_utilisateur(grille_finale)

def choix_utilisateur_version2(grille):
    """
    Fonction qui demande a l'utilisateur quelle grille il veut afficher entre la pleine et la vide
    Entree : grille de base non travaillee
    Sortie : grille pleine ou vide ou aucun affichage si une valeur differente de 1 ou 2
    """
    choix = int(input("Inserez 1 pour voir la grille de départ. Inserez 2 pour voir la grille pleine."))
    if choix == 1:
        print(affichage_version2(grille))
    elif choix == 2:
        print(affichage_version2(ecoulement(grille, len(grille))))
    else:
        print("il fallait choisir 1 ou 2 ...")


grille_finale = generer_grille(L2)
choix_utilisateur_version2(grille_finale)
