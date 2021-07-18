from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        # not use it as constant, as it's changing at the bouncing logic
        # while loop can continue to call move()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto((x_cor + self.x_move, y_cor + self.y_move))

    # ball bouncing on upper and lower wall
    def bounce_y(self):
        # if only .goto(self.x_cor(), self.y_cor() - 10) it will only reduce y cor for the first time
        # this way, it goes continuously
        # inverting values work for both sides, at left side, the y_cor will increase,
        # as it is at the negative side of y
        self.y_move *= -1

    # detect collision at the paddle
    def bounce_x(self):
        # decrease x cor at the right side,
        # as y cor will increase when calling move(), because the y_cor + y_move
        self.x_move *= -1
        # increase speed when hit a paddle, but it will never go to 0
        self.speed *= 0.9

    def reset_position(self):
        self.home()
        #  once back to 0,0, go to the opposite direction
        self.bounce_x()
        # reset to initial speed
        self.speed = 0.1



