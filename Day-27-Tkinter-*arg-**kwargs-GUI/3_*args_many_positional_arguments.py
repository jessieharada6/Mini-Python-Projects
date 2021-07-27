
#TODO: Unlimited arguments - allow any number of inputs for methods
# ASSIGN BY POSITION otherwise default, ORDER/POSITION matters
#TODO: args can be named as anything, but mandatory key word is *
# *arg s-> tuple
# args[1]
# for arg in args:

def add(*args):
    sum = 0
    # *args is a tuple - <class 'tuple'>, therefore can iterate
    print(type(args))
    # can access by position
    print(args[1])
    for n in args:
        sum += n
    return sum


sum = add(3, 100, 6, 2, 5, 7, 8, 2, 5, 6, -1)
print(sum)

# in js, it is spread operator (...)