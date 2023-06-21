from turtle import Screen, Turtle
from random import randint
display_surface = Screen()
display_surface.bgcolor('black')
display_surface.title("Snake Game")
display_surface.setup(width=600, height=600)


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


snake_head = make_turtle("square", "blue")
snake_food = make_turtle("circle", "red")
change_food_position()


running = True
while running:
    display_surface.update()
