
#TODO: arbitary number of keyword arguments - keyword args
# ASSIGN BY NAME otherwise null (must use .get()) otherwise error (if use ["key"], NAME matters
#TODO: kwargs can be named as anything, but mandatory key word is **
# **kwargs -> dictionary
# kwargs.get("key")
# for (key, value) in kwargs.items()

def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # can iterate
    for key, value in kwargs.items():
        print(key)
        print(value)
    # can access
    print(kwargs["add"])

calculate(add=3, multiply=5)

def calculate1(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate1(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # use [] for key, when user did not pass in a property, it returns an error
        # self.make=kw["make"]
        # self.mode=kw["model"]
        # use .get() so when user did not pass in a property, it returns null
        self.make =kw.get("make")
        self.model =kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# my_car = Car(make="Nissan", model="GWT")
my_car = Car(make="Nissan")
print(my_car.model)


# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
# all_aboard(4, 7, 3, 0, x=10, y=64)
# What is the output of the code above?
# Answer: 4 is passed by position. 7,3,0 are collected into a tuple. x and y are in a keyword dictionary
# 4 (7, 3, 0) {'x' : 10, 'y' : 64}


# What is the output of this code?
#
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
# bar(1, 2)
# Answer: The optional arguments, toast and ham, get assigned their default values.
# 1 2 'yes please!' 0

# What is the output of this code?
#
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
# bar(toast='nah', spam=4, eggs=2)
# Answer: When keywords are used the order of the arguments listed does not matter.
# Python matches by name not position.
# 4 2 'nah' 0

# def test(*args):
#     print(args)
#
# test(1,2,3,5)
# What is the data type of args?
# Answer: tuple

# def test(*args):
#     print(args)
#
# test(1,2,3,5)
#
# What is the output of the code above?
# Answer: args is a tuple, hence it will print the parenthesis.
# (1, 2, 3, 4)