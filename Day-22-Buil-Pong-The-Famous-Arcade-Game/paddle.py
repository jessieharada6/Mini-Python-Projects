from turtle import Turtle
UP = 90
DOWN = 270
MOVING_DISTANCE = 20
PADDLE_1_X = 350
PADDLE_1_Y = -350

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVING_DISTANCE
        # when using variables, see what's available first
        # instead of using paras to pass in
        # once we have position as a tuple
        # we get self.xcor() and self.ycor() naturally
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVING_DISTANCE
        self.goto(self.xcor(), new_y)

