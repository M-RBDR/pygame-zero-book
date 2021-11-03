import random

n = random.randint(0, 10)

print("Qu'est-ce que", n, "plus 7?")
g = int(input())  # Pourquoi est ce qu'on utilise int() ici?
if g == n + 7:
    print("C'est bien ça")
else:
    print("Faux")
