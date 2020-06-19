import turtle

STEP_SIZE = 20

# initialize screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.bgcolor("#B2FF66")

# initialize turtle
snake_head = turtle.Turtle()
snake_head.color("#006633")
snake_head.shape("square")
snake_head.penup()


def go_right():
    x = snake_head.xcor()
    snake_head.setx(x + STEP_SIZE)


def go_left():
    x = snake_head.xcor()
    snake_head.setx(x - STEP_SIZE)


# keyboard bindings
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

window.listen()  # listen to keyboard inputs

window.mainloop()  # keep screen open
