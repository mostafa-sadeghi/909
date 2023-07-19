from turtle import Screen, Turtle
from random import randint


def make_screen(color, w, h):
    window = Screen()
    window.bgcolor(color)
    window.title("Snake Game")
    window.setup(width=w, height=h)
    window.tracer(False)
    return window


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.speed("fastest")
    my_turtle.penup()
    return my_turtle


def change_food_position(snake_food):
    xposition = randint(-280, 280)
    yposition = randint(-280, 230)
    snake_food.goto(xposition, yposition)


def reset(snake_head, tails):
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for tail in tails:
        tail.hideturtle()

    tails.clear()
