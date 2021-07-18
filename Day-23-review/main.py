import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")
cars = CarManager()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    # player wins
    if player.at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        cars.speed_up()

    # player hits car
    for car in cars.car_list:
        if player.distance(car) <= 20:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()