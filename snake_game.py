from turtle import Screen, Turtle
from random import randint

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

# TODO  تعریف سه تابع دیگر برای جهت های چپ، راست و پائین

display_surface.listen()
display_surface.onkeypress(change_dir_to_up, "w")
# اضافه کردن مدیریت کننده رویداد برای دکمه های 
# asd
# a => چپ

snake_head = make_turtle("square", "blue")
snake_food = make_turtle("circle", "red")
snake_head.direction = ""
change_food_position()


running = True
while running:
    display_surface.update()
