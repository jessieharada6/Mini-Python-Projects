print("print('what to print')")
print('print(\'what to print\')')

print('The function is declared like this:\nhello')

# no space after \n
print('The function is declared like this:\nhello')

# same code below
name = input("What is your name?")
print('Hello ' + name)
# -----
print('Hello' + input("What is your name?"))

# same code below
name = input("What is your name?")
print(len(name))
# -----
print(len(input("What is your name?")));

# swap
a = input("a: ")
b = input("b: ")

#  swap a and b
temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")

#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet);
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/