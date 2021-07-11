###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random as r

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb = color.rgb
#     rgb_colors.append((rgb.r, rgb.b, rgb.g))

# get from rgb_colors, removed the first three background colors
color_list = [(202, 109, 164), (238, 245, 240), (150, 49, 75), (223, 135, 201), (52, 124, 93), (172, 40, 154), (140, 19, 30), (133, 185, 163), (198, 71, 91), (46, 86, 122), (72, 35, 43), (145, 148, 178), (13, 71, 99), (233, 164, 175), (161, 158, 142), (105, 77, 74), (55, 50, 46), (183, 171, 205), (36, 74, 60), (18, 90, 86), (81, 129, 148), (148, 20, 17), (14, 64, 70), (30, 100, 68), (107, 153, 127), (174, 97, 94), (176, 209, 192)]

t.colormode(255)

hirst = t.Turtle()
#set turtle to the a point so can see it starts
hirst.penup()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

def draw_art():
    for _ in range (10):
        rgb = r.choice(color_list)
        hirst.color(rgb)
        hirst.dot(20)
        hirst.penup()
        hirst.fd(50)
        hirst.pendown()

def next_row():
    hirst.penup()
    hirst.setheading(90)
    hirst.forward(50)
    # seems always set based on 0 coordinates even if it's changed before
    hirst.setheading(180)
    hirst.forward(500)
    hirst.setheading(0)

for _ in range(10):
    draw_art()
    next_row()
# hirst.speed("slowest")
# hirst.setheading(90)
# hirst.forward(50)
# hirst.setheading(180)

# happen after all movements of turtle
screen = t.Screen()
screen.exitonclick()