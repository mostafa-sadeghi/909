from turtle import Screen, Turtle
from random import randint
from time import sleep


def make_screen(color, w, h):
    window = Screen()
    window.bgcolor(color)
    window.title("Snake Game")
    window.setup(width=w, height=h)
    return window


display_surface = make_screen("black", 600, 600)


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.speed("fastest")
    my_turtle.penup()
    return my_turtle


def change_food_position():
    xposition = randint(-280, 280)
    yposition = randint(-280, 280)
    snake_food.goto(xposition, yposition)


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
change_food_position()


running = True
while running:
    display_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position()
    move_snake()
    sleep(0.2)
