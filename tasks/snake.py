import turtle
import time

# for detailed documentation of "Turtle graphics" library see:
# https://docs.python.org/3/library/turtle.html

# head directions
HEAD_DIRECTION_UP = 0
HEAD_DIRECTION_DOWN = 1
HEAD_DIRECTION_LEFT = 2
HEAD_DIRECTION_RIGHT = 3

STEP_SIZE = 20  # default size of the turtle is 20x20
snake_head_direction = HEAD_DIRECTION_RIGHT  # start direction

# settings
update_delay = 0.1  # decrease number for a more difficult game. The snake will then be faster.

# initializing screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.tracer(0)  # Turns off the screen updates
window.bgcolor("#B2FF66")

# creating snake
snake = turtle.Turtle()
snake.color("#006633")
snake.shape("square")
snake.penup()


# Functions
def go_up():
    global snake_head_direction
    if snake_head_direction != HEAD_DIRECTION_DOWN:
        snake_head_direction = HEAD_DIRECTION_UP


def go_down():
    global snake_head_direction
    if snake_head_direction != HEAD_DIRECTION_UP:
        snake_head_direction = HEAD_DIRECTION_DOWN


def go_left():
    global snake_head_direction
    if snake_head_direction != HEAD_DIRECTION_RIGHT:
        snake_head_direction = HEAD_DIRECTION_LEFT


def go_right():
    global snake_head_direction
    if snake_head_direction != HEAD_DIRECTION_LEFT:
        snake_head_direction = HEAD_DIRECTION_RIGHT


def move():
    direction = snake_head_direction
    x = snake.xcor()
    y = snake.ycor()

    if direction == HEAD_DIRECTION_RIGHT:
        x += STEP_SIZE
    elif direction == HEAD_DIRECTION_LEFT:
        x -= STEP_SIZE
    elif direction == HEAD_DIRECTION_UP:
        y += STEP_SIZE
    elif direction == HEAD_DIRECTION_DOWN:
        y -= STEP_SIZE

    if check_for_collision(x, y):
        return False

    snake.setposition(x, y)

    return True


def check_for_collision(x, y):
    snake_collided = False

    if (x >= SCREEN_WIDTH / 2) or (x <= -(SCREEN_WIDTH / 2)):
        snake_collided = True
    elif (y >= SCREEN_HEIGHT / 2) or (y <= -(SCREEN_HEIGHT / 2)):
        snake_collided = True

    return snake_collided


def play():
    # Main game loop
    play_game = True
    while play_game:
        if not move():
            play_game = False

        window.update()
        time.sleep(update_delay)


# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")
window.onkeypress(play, "p")

# initialize screen with turtle
window.update()

window.mainloop()  # keep screen open
