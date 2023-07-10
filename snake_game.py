from time import sleep
from snake_game_utils import *


display_surface = make_screen("black", 600, 600)
score = 0


def change_dir_to_up():
    snake_head.direction = "up"


def change_dir_to_down():
    snake_head.direction = "down"


def change_dir_to_left():
    snake_head.direction = "left"


def change_dir_to_right():
    snake_head.direction = "right"


def move_snake():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)

    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)

    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)


display_surface.listen()
display_surface.onkeypress(change_dir_to_up, "Up")
display_surface.onkeypress(change_dir_to_down, "Down")
display_surface.onkeypress(change_dir_to_left, "Left")
display_surface.onkeypress(change_dir_to_right, "Right")


snake_head = make_turtle("square", "blue")
snake_food = make_turtle("circle", "red")
snake_head.direction = ""
change_food_position(snake_food)


score_board = make_turtle("square", "white")
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write(f"Score: {score}", font=("arial", 30), align="center")

running = True
while running:
    display_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
    move_snake()
    sleep(0.2)
