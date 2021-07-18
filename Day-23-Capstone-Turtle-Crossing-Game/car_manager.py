from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        # it is a list of cars, make this a property for the object to access
        self.car_list = []

    # CHALLENGING PART - code comment: create multiple cars
    # create one object - random on the y_cor, and add to the list
    # trick is:
    # in the main, in while loop, it continuously creates cars
    def create_cars(self):
        # code comment:
        # create intervals of creating new cars in the while loop
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_y_cor = random.randint(-280, 280)
            new_car.goto((300, new_y_cor))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.bk(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
