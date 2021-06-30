# random module
# import module
# module.method
#[0.0, 1.0)
random_float = random.random()
print(random_float)

#[0.0, 1.0) * 5: [0.0, 5.0)
random_decimal = random.random() * 5
print(random_decimal)

import random
random_int = random.randint(0, 1)

if random_int == 1:
  print("Heads")
else:
  print("Tails")

# Data Structure: Python List
# Ordered, data type can mix
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
fruits = [True, "Ras", "Berry", 1]
print(fruits[0])
print(fruits[-1]) #count from the back
print(fruits[-2]) # "Berry"
fruits[0] = "Banana" #Update
fruits.append(["Blue", "try"]) # Add one item, can add as an array
fruits.extend(["Ship", "Winds", "Gardens"]) # add a list
print(fruits) #['Banana', 'Ras', 'Berry', 1, ['Blue', 'try'], 'Ship', 'Winds', 'Gardens']

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # string to array
#Angela, Ben, Jenny, Michael, Chloe
len = len(names)
random_pick = random.randint(0, len - 1)
print(f"{names[random_pick]} is going to buy the meal today")

# 2D
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row = int(position[1]) - 1
column = int(position[0]) - 1
map[row][column] = 'x'