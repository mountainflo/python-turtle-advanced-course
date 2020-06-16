import turtle

'''
Aufgabe: Keyboard-Bindings kennen lernen

Ersetze alle TODO-Kommentare mit den richtigen Python-Befehlen.
Am Ende soll sich die Schlange über die Pfeiltasten nach links
und rechts über das Spielfeld bewegen können.
'''

# initialize screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# initialize turtle
snake_head = turtle.Turtle()
snake_head.color("#006633")
snake_head.shape("square")
snake_head.penup()


def go_right():
    # TODO: x-position der Schlange abfragen
    # TODO: x-postion um 20 nach rechts verschieben
    # TODO: neue x-position für Schlange setzen


def go_left():
    # TODO: x-position der Schlange abfragen
    # TODO: x-postion um 20 nach links verschieben
    # TODO: neue x-position für Schlange setzen


# keyboard bindings
# TODO: window.onkey() verwenden und go_right an rechte-Pfeiltaste binden
# TODO: window.onkey() verwenden und go_left an linke-Pfeiltaste binden

window.listen()  # listen to keyboard inputs

window.mainloop()  # keep screen open
