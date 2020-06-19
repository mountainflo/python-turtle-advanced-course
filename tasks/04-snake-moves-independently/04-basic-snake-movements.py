import turtle
import time

STEP_SIZE = 20
update_delay = 0.2  # decrease number for a more difficult game. The snake will then be faster.

# head directions
HEAD_DIRECTION_LEFT = 0
HEAD_DIRECTION_RIGHT = 1

snake_start_direction = HEAD_DIRECTION_RIGHT  # turtle default value
snake_head_direction = snake_start_direction

# initialize screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.bgcolor("#B2FF66")
window.tracer(0)  # Turns off the screen updates

# initialize turtle
snake_head = turtle.Turtle()
snake_head.color("#006633")
snake_head.shape("square")
snake_head.penup()


def go_left():
    global snake_head_direction
    snake_head_direction = HEAD_DIRECTION_LEFT


def go_right():
    global snake_head_direction
    snake_head_direction = HEAD_DIRECTION_RIGHT


# keyboard bindings
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

window.listen()  # listen to keyboard inputs

while True:
    direction = snake_head_direction
    x = snake_head.xcor()
    if direction == HEAD_DIRECTION_RIGHT:
        snake_head.setx(x + STEP_SIZE)
    else:
        snake_head.setx(x - STEP_SIZE)

    window.update()
    time.sleep(update_delay)
