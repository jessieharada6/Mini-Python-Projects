from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        interval = random.randint(1, 6)
        if interval == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            y_cor = random.randint(-280, 280)
            car.goto((300, y_cor))
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT