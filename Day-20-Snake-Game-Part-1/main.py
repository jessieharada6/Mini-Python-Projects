from turtle import Screen, Turtle
import time
from snake import Snake
# https://docs.python.org/3/library/turtle.html

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# animate snake segments: turn animation off, screen will refresh when .update()
screen.tracer(0)

# create snake body
snake = Snake()

# control snake with a key press
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    # animate snake segments: update screen
    screen.update()
    time.sleep(0.5)
    # get snake to move
    snake.move()

screen.exitonclick()
