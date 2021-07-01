# Functions with Inputs
# name: paramter (name of the data) 
def greet(name):
    print("Welcome")
    print(f"Hello {name}")

# "Jessie": argument (actual data)
greet("Jessie")


# Multiple Arguments
def greet_with(name, location):
    print(f"Hi {name} from {location}")

# positional arguments: check based on the positions
greet_with("Jessie", "Sydney")
# keyword arguments: check based on the values assigned to the params
greet_with(location = "Singapore", name = "Kiyomi")


# Paint Area Calculator
#Write your code below this line 👇
import math 
def paint_calc(height, width, cover):
    return math.ceil((height * width) / cover)

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"You will need {paint} cans of paint")

