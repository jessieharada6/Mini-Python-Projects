# DATA TYPES

# string
# subscript
# print(len(123456)) won't work
print("Hello"[0]) #H
print("Hello"[len("Hello") - 1]) #o
print(len("123")) #3
print("123" + "345") #123345 as string

# integer
print(123 + 345) #468
print(123_456_789) #123456789 - 123,456,789 can be written

#float
print(3141.59)
print(734_529.678)

#boolean
print(True) #capital cases
print(False)


# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name"))
# it is an integer, can't use + as concat the string
print("name has ", num_char, " characters")

#TYPE Checking
print(type(num_char)) #<class 'int'>

#Type Conversion
new_num_char = str(num_char) #convert to string
print(type(new_num_char)) #<class 'str'>
print("name has " + new_num_char + " characters")


#convert string to float, then add the integer
print(70 + float(""100.5"")) #170.5
print(str(70) + str(100)) #70100"


# Mathematical Operations in Python
#PEMDAS: () ** *,/ +,-
print(type(6 / 3)) # <class 'float'>
print(2 ** 3) # 2 ^ 3
print(3 * 3 + 3 / 3 - 3) #7.0 float

# Number Manipulation and F Strings in Python
print(round(8 / 3)) #2
print(round(8 / 3, 2)) #2.67 float with 2 decimal points
print(8 // 3) #2

score = 0
height = 1.8
isWinning = True
#f-string
print(f"your score is {score}, your height is {height}, your winning is {isWinning}")

# F string practice
age = input("What is your current age?")

age_as_int = int(age)
years_remaining = 90 - age_as_int
age_in_months = years_remaining * 12;
age_in_weeks = years_remaining * 52
age_in_days = years_remaining * 365

print(f'You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.')

print(6 + 4 / 2 - (1 * 2)) ==> 6.0