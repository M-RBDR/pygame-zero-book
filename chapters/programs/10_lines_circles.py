WIDTH = 500   # Que sont ces valeurs? Qu'arrive-t-il si on les changes?
HEIGHT = 500  # Qu'est-ce qui arrive si on supprime cette ligne?


def draw():
    screen.clear()
    screen.draw.circle((250, 250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "red")
    screen.draw.line((150, 20), (150, 450), "purple")
    screen.draw.line((150, 20), (350, 20), "purple")

