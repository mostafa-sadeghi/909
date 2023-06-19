from turtle import Screen, Turtle
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

snake_head = make_turtle("square","blue")
snake_head.goto(100,100)

# TODO    برای غذا یک ترتل دایره ای قرمز اضافه کنید


running = True
while running:
    display_surface.update()

