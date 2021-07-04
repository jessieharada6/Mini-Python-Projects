is_true = False
a  = 31
b = 25
while not is_true:
    c = a + b
    print(c)
    if a == b:
        print("a = b")
    elif a > b:
        print("a > b")
        # is_true = True
    elif a < b:
        print("a < b")
        is_true = True