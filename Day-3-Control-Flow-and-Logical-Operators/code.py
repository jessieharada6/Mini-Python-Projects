# if else
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

# Nested if statements and elif statements
# if condition1:
# elif condition2:
# elif condition3:
# elif condition4:
# else:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("How old are you? "))
  if age > 18:
    print("The ticket price is $12")
  elif age <= 18 and age > 12:
    print("The ticket price is $7")
  else:
    print("The ticket price is $5")
else:
  print("Sorry")


# if condition1:
# if condition2:
# if condition3:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")

  age = int(input("How old are you? "))
  if age > 18:
    print(f"The ticket price is $12")
    bill = 12;
  elif age <= 18 and age > 12:
    print(f"The ticket price is $7")
    bill = 7
  else:
    print(f"The ticket price is $5")
    bill = 5
  
  photo = input("Do you want photos?")
  if photo == "Y":
    bill += 3
  print(f"Total bill is ${bill}")
  
else:
  print("Sorry")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "L":
  bill += 25
  if add_pepperoni == "Y":
    bill += 3
elif size == "M":
  bill += 20
  if add_pepperoni == "Y":
    bill += 3
elif size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
  bill += 1

print(f"Total bill is ${bill}")

# Logical Operator:

# A and B
# C or D
# not E
