# slice [a, b)
# [1 :], [:5], [2:5]
# [3:5:2], 2 is every other number increment
# [::2], go every other number for the whole list
# [::-1] start from the end, and go to the beginning


piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuples = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[1:])
print(piano_keys[:5])
print(piano_keys[2:5])
print(piano_keys[1:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])

print(piano_tuples[2:5])