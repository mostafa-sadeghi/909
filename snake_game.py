import turtle
from time import sleep
from snake_game_utils import *
from tkinter import Button

display_surface = make_screen("black", 600, 600)
score = 0

try:
    f = open("snake_score.txt", "r")
    high_score = int(f.read())
except:
    f = open("snake_score.txt", "w")
    high_score = 0

finally:
    f.close()


# def my_func(x,y):
#     print("blalallala")
# my_turtle = turtle.Turtle()
# my_turtle.shape("square")
# my_turtle.color("grey")
# my_turtle.penup()
# my_turtle.shapesize(2, 4)
# my_turtle.goto(-260, 280)
# my_turtle.onclick(my_func)
# def onclick():
#     snake_head.direction = ""
# my_button = Button(display_surface._root, text="hello",command=onclick, background="red", foreground="yellow")
# my_button.place(x=20, y=20)

def onclose():
    try:
        f = open("snake_score.txt", "w")
        f.write(str(high_score))
    except:
        print("error")
    finally:
        f.close()
    global running
    running = False


root = display_surface._root
root.protocol("WM_DELETE_WINDOW", onclose)


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

snake_tails = []

running = True
while running:
    score_board.clear()
    score_board.write(f"Score: {score}, HighScore:{high_score}",
                      font=("arial", 30),
                      align="center")
    display_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_food_position(snake_food)
        score += 1
        new_tail = make_turtle("square", "cyan")
        snake_tails.append(new_tail)

        if score > high_score:
            high_score = score

    if snake_head.xcor() > 290 or \
            snake_head.xcor() < -290 or \
            snake_head.ycor() > 240 or snake_head.ycor() < -290:
        reset(snake_head, snake_tails)
        try:
            f = open("snake_score.txt","w")
            f.write(str(high_score))
        except:
            print("error")
        finally:
            f.close()
        score = 0

    for i in range(len(snake_tails) - 1, 0, -1):
        xpos = snake_tails[i - 1].xcor()
        ypos = snake_tails[i - 1].ycor()
        snake_tails[i].setpos(xpos, ypos)

    if len(snake_tails) > 0:
        xhead = snake_head.xcor()
        yhead = snake_head.ycor()
        snake_tails[0].setpos(xhead, yhead)

    move_snake()

    sleep(0.2)
