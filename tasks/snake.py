import turtle
import time
from random import randint

# for detailed documentation of "Turtle graphics" library see:
# https://docs.python.org/3/library/turtle.html

# head directions
HEAD_DIRECTION_UP = 0
HEAD_DIRECTION_DOWN = 1
HEAD_DIRECTION_LEFT = 2
HEAD_DIRECTION_RIGHT = 3

# settings
update_delay = 0.2  # decrease number for a more difficult game. The snake will then be faster.
snake_color = "#006633"

STEP_SIZE = 20  # default size of the turtle is 20x20
snake_start_direction = HEAD_DIRECTION_RIGHT
snake_head_direction = snake_start_direction


# initialize screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
window = turtle.Screen()
window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
window.tracer(0)  # Turns off the screen updates
window.bgcolor("#B2FF66")

# create the game elements
snake_head = turtle.Turtle()
snake_head.color(snake_color)
snake_head.shape("square")
snake_head.penup()

snake = [snake_head]

fruit = turtle.Turtle()
fruit.color("red")
fruit.shape("square")
fruit.penup()


def initialize_board():
    global snake, snake_head_direction

    # remove all body elements of the previous game
    for elem in snake[1:]:
        elem.hideturtle()
        del elem

    snake = [snake_head]
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
    x = snake_head.xcor()
    y = snake_head.ycor()
    x_old = x
    y_old = y

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

    # check if snake bite itself
    if check_for_collision_in_list(x, y, snake[1:]):
        return False

    # check if snake hits a fruit
    if check_for_collision_in_list(x, y, [fruit]):

        # replace head with new body element
        snake_body_elem = turtle.Turtle()
        snake_body_elem.color(snake_color)
        snake_body_elem.shape("square")
        snake_body_elem.penup()
        snake_body_elem.setposition(x_old, y_old)

        snake.insert(1, snake_body_elem)

        # place new random fruit on the board
        place_fruit()
    else:
        # move last element to old head position
        if len(snake) > 1:
            snake_tail = snake[-1]
            del snake[-1]
            snake_tail.setposition(x_old, y_old)
            snake.insert(1, snake_tail)

    snake_head.setposition(x, y)

    return True


def check_for_collision_in_list(x, y, turtle_obj_list):
    collision = False

    for elem in turtle_obj_list:
        if elem.xcor() == x and elem.ycor() == y:
            collision = True

    return collision


def check_for_collision_with_boundaries(x, y):
    snake_collided = False

    if (x >= SCREEN_WIDTH / 2) or (x <= -(SCREEN_WIDTH / 2)):
        snake_collided = True
    elif (y >= SCREEN_HEIGHT / 2) or (y <= -(SCREEN_HEIGHT / 2)):
        snake_collided = True

    return snake_collided


def play():
    initialize_board()
    print("The game starts. Let´s play ...")

    # Main game loop
    play_game = True
    while play_game:
        if not move():
            play_game = False

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

        if not check_for_collision_in_list(x, y, snake):
            placed_fruit = True
            fruit.setposition(x, y)


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

print("Start the game by pressing 'p'")

window.mainloop()  # keep screen open
