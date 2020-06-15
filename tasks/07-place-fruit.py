import turtle
import time
from random import randint

STEP_SIZE = 20
update_delay = 0.13  # decrease number for a more difficult game. The snake will then be faster.

# head directions
HEAD_DIRECTION_UP = 0
HEAD_DIRECTION_DOWN = 1
HEAD_DIRECTION_LEFT = 2
HEAD_DIRECTION_RIGHT = 3

snake_start_direction = HEAD_DIRECTION_RIGHT  # turtle default value
snake_head_direction = snake_start_direction

# initialize screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.bgcolor("#B2FF66")
window.tracer(0)  # Turns off the screen updates

# create the game elements
snake_head = turtle.Turtle()
snake_head.color("#006633")
snake_head.shape("square")
snake_head.penup()

fruit = turtle.Turtle()
fruit.color("red")
fruit.shape("square")
fruit.penup()


def initialize_board():
    global snake_head_direction

    snake_head.setposition(0, 0)
    snake_head_direction = snake_start_direction
    place_fruit()


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
    snake_head_direction = HEAD_DIRECTION_UP


def go_down():
    global snake_head_direction
    snake_head_direction = HEAD_DIRECTION_DOWN


def go_left():
    global snake_head_direction
    snake_head_direction = HEAD_DIRECTION_LEFT


def go_right():
    global snake_head_direction
    snake_head_direction = HEAD_DIRECTION_RIGHT


def move():
    direction = snake_head_direction
    x = snake_head.xcor()
    y = snake_head.ycor()

    if direction == HEAD_DIRECTION_RIGHT:
        x += STEP_SIZE
    elif direction == HEAD_DIRECTION_LEFT:
        x -= STEP_SIZE
    elif direction == HEAD_DIRECTION_UP:
        y += STEP_SIZE
    elif direction == HEAD_DIRECTION_DOWN:
        y -= STEP_SIZE

    if check_for_collision_with_boundaries(x, y):
        return False

    # check if snake hits a fruit
    if check_for_collision_with_turtle_obj(x, y, fruit):
        # place new random fruit on the board
        place_fruit()

    snake_head.setposition(x, y)

    return True


def check_for_collision_with_boundaries(x, y):
    snake_collided = False

    if (x >= SCREEN_WIDTH / 2) or (x <= -(SCREEN_WIDTH / 2)):
        snake_collided = True
    elif (y >= SCREEN_HEIGHT / 2) or (y <= -(SCREEN_HEIGHT / 2)):
        snake_collided = True

    return snake_collided


def play():
    initialize_board()
    print("The game starts. Let us play ...")

    play_game = True
    while play_game:
        play_game = move()

        window.update()
        time.sleep(update_delay)

    print("GAME OVER!")


def place_fruit():
    global fruit

    placed_fruit = False

    while not placed_fruit:

        border_space = STEP_SIZE
        half_screen_width = (SCREEN_WIDTH - border_space) / 2
        half_screen_height = (SCREEN_HEIGHT - border_space) / 2

        width = int(half_screen_width / STEP_SIZE)
        height = int(half_screen_height / STEP_SIZE)

        x = randint(-width, width) * STEP_SIZE
        y = randint(-height, height) * STEP_SIZE

        if not check_for_collision_with_turtle_obj(x, y, snake_head):
            placed_fruit = True
            fruit.setposition(x, y)


def check_for_collision_with_turtle_obj(x, y, turtle_obj):
    collision = False

    if turtle_obj.xcor() == x and turtle_obj.ycor() == y:
        collision = True

    return collision


# draw border
draw_screen_border()

# keyboard bindings
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(play, "p")

window.listen()  # listen to keyboard inputs

# initialize screen with turtle
window.update()

print("Start the game by pressing 'p'")

window.mainloop()  # keep screen open