# Code Exercise:  Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

####################################
#Write your code below this line 👇
sum = 0;
for d in two_digit_number:
  sum += int(d)

print(sum)

# Code Exercise: BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

fWeight = float(weight)
fHeight = float(height)
bmi = fWeight / (fHeight ** 2)
bmi_as_int = int(bmi)
print(bmi_as_int)

# Day 2 Project: Tip Calculator
print("Welcome to the tip calculator")
bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
num_of_ppl = input("How many people to split the bill?\n")

tip_num = (int(tip)/100  + 1)
result = (float(bill) / int(num_of_ppl)) * tip_num
print(f"Each person should pay: ${round(result, 2)}")