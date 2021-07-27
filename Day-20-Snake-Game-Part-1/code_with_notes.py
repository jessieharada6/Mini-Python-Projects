# list_comprehension.py
from turtle import Screen, Turtle
import time
from snake import Snake
# https://docs.python.org/3/library/turtle.html

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# turn animation off, screen will refresh when .update()
screen.tracer(0)

snake = Snake()

# Control Snakes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # delay by 0.1 s and move as the entire piece
    screen.update()
    time.sleep(0.3)
    snake.move()

# segment_1 = Turtle("square")
# segment_1.color("white")
# # print(segment_1.pos())
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x=-20, y =0)
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x=-40, y =0)



screen.exitonclick()




# snake.py
from turtle import Screen, Turtle

# constant - outside of class
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            # self. refers to the attributes
            self.segments.append(new_segment)

    def move(self):
        # start= len(segments) - 1, stop = 0, step = -1
        # but range function does not use param arguments
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # let the 2nd seg go to 1st seg
            # let the 1st seg go to 0 seg
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # now update the 0 seg and the rest of the two follows
        self.head.forward(MOVE_DISTANCE)
        # print(self.segments[0].heading())
        # self.segments[0].left(90)
        # print(self.segments[0].heading())

    def up(self):
        # as we can only move head, not head and tail
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # the rest body follows as .move() being called in main

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)