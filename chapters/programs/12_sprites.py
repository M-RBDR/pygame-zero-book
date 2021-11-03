WIDTH = 500
HEIGHT = 500

extraterrestre = Actor('extraterrestre')
extraterrestre.x = 0
extraterrestre.y = 50


def draw():
    screen.clear()
    extraterrestre.draw()


def update():
    extraterrestre.x += 2
    if extraterrestre.x > WIDTH:
        extraterrestre.x = 0

