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
update_delay = 0.15  # decrease number for a more difficult game. The snake will then be faster.

# initializing screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.tracer(0)  # Turns off the screen updates
window.bgcolor("#B2FF66")

# creating snake
snake = turtle.Turtle()
snake.color("#006633")
snake.shape("square")
snake.penup()


def draw_screen_border():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("black")
    pen.pensize(4)
    pen.penup()
    pen.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    pen.pendown()

    for i in range(2):
        pen.right(90)
        pen.forward(SCREEN_HEIGHT)
        pen.right(90)
        pen.forward(SCREEN_WIDTH)


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

    print("GAME OVER!")


# draw border
draw_screen_border()

# Keyboard bindings
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")
window.onkey(play, "p")

# initialize screen with turtle
window.update()

window.mainloop()  # keep screen open
