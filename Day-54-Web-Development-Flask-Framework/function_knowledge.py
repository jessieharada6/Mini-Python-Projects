#0. function can have inputs, functionality and outputs

#1 . python function is the first class objects
# can be passed as arguments like integer, string, float etc.
# function without brackets
# def calculator(calc_func, n1, n2):
# pass
# calculator(add, n1, n2)
# calculator(multiply, n1, n2)

# 2. nested functions
def outer_function():
    print("outer")
    def nested_function():
        print("inner")
    nested_function()
outer_function()
#from the outside
# nested function is owned by the outer_function
# can only be accessed via outer_function
# if calling nested_function() at the same level as outer_function, will be errored out

# 3. Functions can be returned from other functions
def outer_function():
    print("outer")
    def nested_function():
        print("inner")
    return nested_function
inner = outer_function() #print outer
inner() #print inner
# outer_function() executes print("outer") so it prints
# and save a ref to  inner due to return nested_function
# then inner() executes nested_function()

## python decorator function
# function that has another function wrapped inside
# which gives this decorator extra functionality
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do something before the function that has the decorator being called
        function()
        #do something after the function that has the decorator being called
    return wrapper_function

@delay_decorator
def hello():
    print("hello")

@delay_decorator
def greet():
    print("greet")

hello()
greet()

#@delay_decorator is syntax sugar
# is the same as
# func_with_deco = delay_decorator(greet)
# func_with_deco()