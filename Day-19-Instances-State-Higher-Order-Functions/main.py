from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_positions = -100
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions)
    y_positions += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        # as turtle itself is 40
        if turtle.xcor() == 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your turtle won! The {winning_color} turtle is the winner")
            else:
                print(f"Your turtle lost! The {winning_color} turtle is the winner")
            is_race_on = False


screen.exitonclick()