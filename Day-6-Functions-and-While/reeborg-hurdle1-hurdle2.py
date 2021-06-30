#hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(0, 6):
    jump()

#the for loop above can be written as 

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
   # number_of_hurdles-- won't work
    number_of_hurdles -= 1

# hurdle 2
# if goal is not certain

while not at_goal():
    jump()