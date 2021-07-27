# TODO: Setting Default Values for Optional Arguments inside a Function Header
# Advanced Python Arguments:

# A. arguments with default values
# keyword arguments: def my_function(a= 1, b= 2, c=3)
# if need to to default, just call my_function()
# or if need to change a param, call my_function(b=3)

# TODO: how to see if a param has a default value in methods
# for methods, if we see
# parameter: type_of_data=...
# means it is optional!

# check out on .write(), that is why we only provide customised requirements,
# as it has the default values for each param alr
import turtle
timmy = turtle.Turtle()
timmy.write()

# Practice
# 1. What is the output of this code?
#
# def foo(a, b=4, c=6):
#     print(a, b, c)
#
# foo(1)
# Answer: 1, 4, 6

# 2. What is the output of this code?
#
# def foo(a, b=4, c=6):
#     print(a, b, c)
#
# foo(4, 9)
# Answer: 4, 9, 6

# 3. What is the output of this code?
#
# def foo(a, b=4, c=6):
#     print(a, b, c)
#
# foo(1, 7, 9)
# Answer: 1, 7, 9

# 4. What is the output of this code?
#
# def foo(a, b=4, c=6):
#     print(a, b, c)
#
# foo(20, c=6)
# Answer: 20, 4, 6



