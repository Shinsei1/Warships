# Créé par Waîl Yeager, le 30/11/2023 en Python 3.7
t1 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

joueur1 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


t2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]


joueur2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



def check(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 1:
                return True
    return False

turn = 0

while True:
    """ Systeme de tour par tour à variable /// """
    if turn % 2 == 0:
        joueur = joueur1
        t = t2
    else:
        joueur = joueur2
        t = t1
    """ /// """

    """Quel joueur joue"""
    if joueur == joueur1 and t == t2:
        a = int(input("Quelle ligne attaquer ?, Joueur 1 : "))
        assert(a >= 0 and a < 10)
        b = int(input("Quel numéro est votre cible ?, Joueur 1 : "))
        assert(b >= 0 and b < 10)
    else:
        a = int(input("Quelle ligne attaquer ?, Joueur 2 : "))
        assert(a >= 0 and a < 10)
        b = int(input("Quel numéro est votre cible ?, Joueur 2 : "))
        assert(b >= 0 and b < 10)
    """///"""

    if joueur[a][b] == 0:
        if t[a][b] == 1:
            joueur[a][b] = "X"
            t[a][b]= "X"
            for e in t :
                print(e)
            print("Vous avez touché continuez !")

            for e in joueur:
                print(e)

            if check(t):
                continue
            if not check(t):
                print("Victoire pour joueur 1" if turn % 2 == 0 else "Victoire pour joueur 2")
                break
            for e in t:
                print(e)

        else:
            print("Raté , Vous finissez le combo")
            for e in joueur:
                print(e)
        turn += 1
    else:
         print("Vous avez déjà attaqué cette position. Choisissez une autre position.")

"""GENERATEUR AUTO"""


import random as rdm

joueur1 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#jai rajouter col2 row2 pour uniformiser le tout en horizontal surtout., conseiller d'utiliser avec choix < 20

def gener(tab,choix):
    for i in range(choix):
        row = rdm.randint(0, 9)

        if row != 9:
            row2 = row + 1
        else:
            row2 = row - 1

        col = rdm.randint(0, 9)
        if col != 9:
            col2 = col + 1
        else:
            col2 = col - 1

        if 1 != tab[row][col]:
            tab[row][col] = 1
            tab[row2][col] = 1
            tab[row][col2] = 1
            tab[row2][col2] = 1

    return tab


a = gener(joueur1,15)
for e in a:
    print(e)



