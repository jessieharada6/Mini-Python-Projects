# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)

# 1. LIST COMPREHENSION
# WORK for Python sequence: list, range, string, tuple
# SYNTAX:
# new_list = [new_item for element in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Jessie"
letters_list = [letter for letter in name]
# turn into list

range_list = [n * 2 for n in range(1, 5)]
# [2, 4, 6, 8]

# Conditional list compression
# [new_item for element in list if test]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
# ['Alex', 'Beth', 'Dave']
upper_long_names = [name.upper() for name in names if len(name) > 5]


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Squaring numbers
squared_numbers = [num**2 for num in numbers]

# filtering even number
even_numbers = [num for num in numbers if num % 2 == 0]

# data overlap
# way 1 of reading in data - i had to add the num as column title
# this is the drawback of pandas if there is no title for the data
# import pandas
# data1 = pandas.read_csv("file1.txt")
# data2 = pandas.read_csv("file2.txt")
# file1_list = data1.num.to_list()
# file2_list = data2.num.to_list()
# # print(file1_list, file2_list)
# result = [num for num in file1_list if num in file2_list]
# print(result)

# way 2
with open("file1.txt") as file:
    file1_data = file.readlines()
with open("file2.txt") as file:
    file2_data = file.readlines()

result = [int(num.strip()) for num in file1_data if num in file2_data]
print(result)
