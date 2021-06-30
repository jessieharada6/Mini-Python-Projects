# random heights of the wall

# hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        move()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()

while not at_goal():
    jump()