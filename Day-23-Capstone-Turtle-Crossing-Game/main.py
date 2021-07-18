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
screen.onkey(player.up, "Up")
cars = CarManager()
level = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    # logic comment: detect when turtle hits the car
    # code comment: cars is treated as an object, but it has car_list as property to iterate
    for car in cars.car_list:
        if player.distance(car) <= 20:
            game_is_on = False
            level.game_over()

    # detect turtle wins
    if player.at_finish_line():
        player.reset_position()
        level.increase_level()
        cars.increase_speed()

screen.exitonclick()