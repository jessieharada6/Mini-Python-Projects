# for loop:
# for item in list:
student_heights = [180, 124, 165, 173, 189, 169, 146]
average = 0;
sum = 0;
count = 0;
for h in student_heights:
  sum += h
  count += 1

average = sum / count
print(average)

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
max = 0
for score in student_scores:
  if (max < score):
    max = score

print(max)

# for item in range(a, b)
# [a, b)
# increase by other number, not 1
# for item in range(a, b, increment)
# for (let i = a; i < b; i++)
for number in range(1, 10):
  print(number) #  1, 2, 3, 4, 5, 6, 7, 8, 9

for number in range(1, 10, 3):
  print(number) #  1, 4, 7

# sum even in range [1, 100]
sum = 0
for num in range(1, 101):
  if num % 2 == 0:
    sum += num

# FizzBuzz
for num in range(1, 16):
  if num % 5 == 0 and num % 3 == 0:
    print('FizzBuzz')
  elif num % 5 == 0: 
    print('Buzz')
  elif num % 3 == 0:
    print('Fizz')
  else:
    print(num)