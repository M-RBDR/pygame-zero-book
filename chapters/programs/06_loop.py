import random

n = random.randint(0, 10)

while True:
    print("Je pense à un nombre, pouvez-vous deviner lequel?")
    g = int(input())
    if g == n:
        break
    else:
        print("Faux")
print("Vous avez trouvé!")
