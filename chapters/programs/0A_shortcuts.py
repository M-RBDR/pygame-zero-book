# f est une façon simple d'insérer des variables dans des chaînes de charactères
score = 56
nom = "Richard"
message = f"{nom} a eu {score} points"
print(message)

# += est une façon simple d'augmenter la valeure d'une variable
score = score + 10  # façon longue
score += 10         # façon simple
print(score)

# deux / veut dire une division d'entier (pas de décimales)
x = 76 // 10
# MODULO est le symbole de pourcentage %. Il signifie faire la division et retourner le reste de la division.
reste = 76 % 10
print(f"76 divisé par 10 est {x} et le reste est {reste}")

WIDTH = 500
a = 502
b = 502
# Modulo est souvent utilisé pour réinitialiser un nombre à zéro
# s'il devient trop grand. Alors au lieu de:
if a > WIDTH:
    a = a - WIDTH
# Vous pouvez simplement faire:
b = b % WIDTH
print(a, b)

# input() prend une chaîne de charactères en argument et l'imprime avant de recevoir de l'information du clavier.
# Au lieu de:
print("Entre un nombre")
nombre = input()
# Vous pouvez avoir une seule ligne:
nombre = input("Entre un nombre")
