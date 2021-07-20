from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# https://docs.python.org/3/library/turtle.html

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# animate snake segments: turn animation off, screen will refresh when .update()
screen.tracer(0)

# create snake body
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    time.sleep(0.1)
    # get snake to move
    snake.move()
    # detect collision with food
    # distance between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #  Detect collision with tail
    for segment in snake.segments[1:]:
        # # if head hit head, we pass, but no need anymore due to slice
        # if segment == snake.head:
        #     pass
        #   If the head collides with any segment in the tail:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
