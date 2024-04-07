
import random

prix = random.randint(1, 1000)
player = 0

while player != prix:
    player = input("Entrez un nombre entre 1 et 1000 : ")
    player = int(player)

    if player == prix:
        print("Gagné")
        break
    elif player < prix:
        print("Plus haut")
    else:
        print("Plus bas")