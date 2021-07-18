from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

# Higher order function
# move_forwards as a callback thats why it does not have () --
# function as input (only pass the name
# onkey() is a higher order function
# only when we press space key, move_forwards() executes
# key words arguments, not position arguments
# screen.onkey(fun= move_forwards, key="space")
# screen.listen()
# screen.exitonclick()

# Etch-a-sketch
# W: forwards, S: backwards, A: counter-clockwise, D: clockwise, C: clear drawing
def move_forward():
    timmy.fd(10)

def move_backward():
    timmy.bk(10)

def counter_clockwise():
    timmy.setheading(timmy.heading() + 10)

def clockwise():
    timmy.setheading(timmy.heading() - 10)

def clear():
    timmy.reset()
    # solution:
    # timmy.clear()
    # timmy.penup()
    # timmy.home()
    # timmy.pendown

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")
screen.listen()
screen.exitonclick()

# Object State
# (e.g. timmy.color = green, timmy.color = purple)
# (e.g. timmy.move())
# Instances: examples/objects
