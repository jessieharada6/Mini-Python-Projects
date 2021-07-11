# brew install python-tk, or pip install
# from turtle import Turtle, Screen
import turtle as t
import random
# from turtle import *
# import turtle
# import turtle as t
import heroes

t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("#87CEFA", "#FFC0CB")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# draw a square
def draw_square():
    for _ in range(4):
        timmy.fd(100)
        timmy.rt(90)

# draw_square()

# from turtle import Turtle, Screen, fd, rt
# def draw_square():
#     for _ in range(4):
#         fd(100)
#         rt(90)

#draw a dashed line
def draw_dashed_line():
    for _ in range (15):
        timmy.fd(10)
        timmy.penup()
        timmy.fd(10)
        timmy.pendown()

# draw_dashed_line()

colors = ["#7FFF00", "#FF1493", "#FFD700", "#000080", "#483D8B", "#FF4500", "#9ACD32"]
def draw_diff_shapes():
    for i in range(3, 11):
        # timmy.pencolor(random.choice(colors))
        for j in range(i):
            timmy.fd(100)
            timmy.rt(360 / i)
            timmy.pencolor(colors[i - 3])
            # timmy.pencolor(random.choice(colors))
# draw_diff_shapes()

def random_walk():
    direction = [0, 90, 180, 270]
    timmy.pensize(15)
    timmy.speed("fastest")
    for _ in range(50):
        timmy.pencolor(random_color())
        timmy.fd(50)
        timmy.setheading(random.choice(direction))
# random_walk()

def draw_spirograph(size):
    timmy.speed("fastest")
    for i in range(int(360 / size) + 1):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)

draw_spirograph(5)

# Tuples - ordered - immutable
# once set can't change the values like lists
# can't delete
# stay constant
my_tuple = (1, 3, 8)
my_tuple[0]
# convert to list
# list(my_tuple)
# List
# [1, 3, 8]




# happen after all movements of turtle
screen = t.Screen()
screen.exitonclick()
