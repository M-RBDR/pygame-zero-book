extraterrestre = Actor('extraterrestre')
extraterrestre.pos = (0, 50)

def draw():
    screen.clear()
    extraterrestre.draw()

def update():
    if keyboard.right:
        extraterrestre.x = extraterrestre.x + 2
    elif keyboard.left:
        extraterrestre.x = extraterrestre.x - 2

