from turtle import Turtle

MOVING_DISTANCE = 10

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.setpos(position)

    def up(self):
        # new_x = self.xcor() + 10
        new_y = self.ycor() + MOVING_DISTANCE
        self.goto((self.xcor(), new_y))

    def down(self):
        # new_x = self.xcor() + 10
        new_y = self.ycor() - MOVING_DISTANCE
        self.goto((self.xcor(), new_y))

