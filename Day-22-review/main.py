from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "a")
screen.onkey(l_paddle.down, "z")

is_game_on = True
while is_game_on:
    screen.update()
    # use ball's property speed to control sleep time
    # logic is wrapped in bounce_x, when paddle hits the ball, increase speed
    # when ball out of bounds and reset, speed goes to the initial speed
    time.sleep(ball.speed)
    ball.move()

    # ball bounce at upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # it is a better name than bounce_wall
        # the class itself does not know what's used for
        # all it is implemented is to reduce y_cor
        ball.bounce_y()

    # detect paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        #  travel towards the middle and when hit paddles, increase speed
        ball.bounce_x()

    #  ball out bounds at right side
    if ball.xcor() > 380:
        ball.reset_position()
        # if right paddle misses ball, left side gets point
        score.increase_l_score()

    #  ball out bounds at left side
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()

screen.exitonclick()