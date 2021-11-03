import random

n = random.randint(0, 100)
tentatives = 0

while True:
    tentatives = tentatives + 1
    print("Je pense à un nombre, pouvez-vous deviner lequel?")
    g = int(input())
    if g == n:
        break
    elif g < n:
        print("Trop bas")
    elif g > n:
        print("Trop haut")
print("C'est bien ça! Vous avez pris", tentatives, "tentatives.")
