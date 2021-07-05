# Namespaces: Local vs. Global Scope

################### Scope ####################

# 1. Local Scope: exist within function
def drink_portion():
    # only valid within the funciton 
    potion_strength = 2
    print(potion_strength)

drink_portion()
# print(potion_strength) # NameError: not defined

# Global scope: 
player_health = 100

def drink_portion1():
    # only valid within the funciton 
    potion_strength = 2
    print(player_health) # 100

drink_portion1()

# ANYTHING THAT I NAME has a namespace, as long as it is a namespace, it has a valid scope

# 2. Does Python have block scope? NO
if 3 > 2:
    # it is not considered as a fence
    a_variable = 10

game_level = 3
enemis = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemis[0]

# the new_enemy variable defined in if statement, while, for (anything with :)
# is accessible outside the if in python
print("new_enemy", new_enemy)

# 3. Modify a global variable 
enemies = "Skeletonnnn"

def increase_enemies():
    # the enemies here is a totally new variable than the one above
  enemies = "Zombiieeee"
  print(f"enemies inside function: {enemies}") # Zombiieeee

increase_enemies()
print(f"enemies outside function: {enemies}") # Skeletonnnn

# If we want to modify a global variable 
a_number = 1

def increase_number_g():
    # not recommended 
    global a_number 
    print(a_number)
    a_number += 2
    print(f"modify global var {a_number}")

increase_number_g()
print(f"global variable being modified {a_number}")

# A better way to modify global variable
b_number = 1

def increase_number_g_p():
    return b_number + 2

b_number = increase_number_g_p()
print(f"global variable being modified properly {b_number}")

# Python Constants and Global Scope
# Global constants: defined and never gonna change again - in CAPITAL_LETTER
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@harada_j"


########################Scope Quiz########################
i = 50
def foo():
    i = 100
    return i
 
i = foo()
print(f"return i as function assigned to i: {i}") #100

i = 50
def foo():
    i = 100
    return i
 
foo()
print(f"i as the global variable not changed: {i}") #50

# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.
def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable) #16
 
bar()
