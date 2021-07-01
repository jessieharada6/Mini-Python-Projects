#Write your code below this line 👇
def prime_checker(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
check = prime_checker(number=n)
if check:
    print("It's a prime number")
else:
    print("It's not a prime number")



