# # file not found
# with open("no_file.txt") as file:
#     file.read()
#
# # ket error
# a_dictionary= {"key" : "value"}
# value = a_dictionary["non_existent_key"]
#
# # index error
# fruit_list= ["apple", "banana", "pear"]
# fruit = fruit_list[3]
#
# # type error
# text = "abc"
# print(text + 6)

# catching exception
# code that might have exception
try:
    pass
# if exception
# except alone avoid all errors which can be too broad
# can add specific error and see error message
except:
    pass
# if no exception
# if any except blocks executes, code inside "else" will not execute
else:
    pass
# carry out no matter what happens
finally:
    pass

# # an example
# try:
#     file = open("non_exist.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["no_key"])
# except FileNotFoundError:
#     # if not there (exception), create one
#     file = open("non_exist.txt", "w")
#     file.write("Something")
#     # print("There was an error")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is an error that i made up")

# raise your own exception
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be 3 meters")

bmi = weight / height ** 2
print(bmi)


