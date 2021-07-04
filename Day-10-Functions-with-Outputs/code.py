# def function():
    # do something
# def function(something):
    #do this with something

# 1. Functions with outputs
#def funciton():
    # return 3 * 2

# output = funciton()
# output = 6

def format_name (firstName, lastName):
    # new_first_name = firstName.capitalize() 
    # new_last_name = lastName.capitalize()
    # return new_first_name + " " + new_last_name
    new_first_name = firstName.title() 
    new_last_name = lastName.title()
    return f"{new_first_name} {new_last_name}"
    
formatted_name = format_name("jesSie", "wAng")
print(formatted_name)

# built-in function with output
output = len("Jessie")
print(output)

# return is the end of the function 

# 2. Multiple return values 
def format_name (firstName, lastName):
    if firstName == "" or lastName == "":
        return f"no valid input provided"
    
    new_first_name = firstName.title() 
    new_last_name = lastName.title()
    return f"{new_first_name} {new_last_name}"
    
formatted_name = format_name("jesSie", "wAng")
print(formatted_name)
empty_name = format_name("", "harada")
print(empty_name)

# built-in function with output
output = len("Jessie")
print(output)

# 3. Docstrings
# explain what the funciton does 
def format_name (firstName, lastName):
    """Take a first and last name, and 
    format it to return the title case version of the name"""
    new_first_name = firstName.title() 
    new_last_name = lastName.title()
    return f"{new_first_name} {new_last_name}"

