from turtle import Turtle

MOVING_DISTANCE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        # initial. speed
        self.move_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto((new_x_cor, new_y_cor))

#     detect ball bounding at upper and lower wall
    def bounce_y(self):
        # move the y coordinate to be minus
        # then in while loop, move() will execute
        self.y_move *= -1

    # bounce at the paddle
    def bounce_x(self):
        self.x_move *= -1
        # increase speed when ball hits at the paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto((self.x_move, self.y_move ))
        self.bounce_x()
        self.move_speed = 0.1





