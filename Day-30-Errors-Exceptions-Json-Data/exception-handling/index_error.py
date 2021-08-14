fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    # if try without exception
    else:
        print(fruit + " pie")


make_pie(4)