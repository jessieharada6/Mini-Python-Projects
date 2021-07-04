from art import logo

# Calculator
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "invalid input"
    return a / b

operations = {
    # key: symbol, value: method
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
}

def calculator():
    # print(logo)
    num1 = float(input("What is the first number? \n"))
    for ops in operations:
        print(ops)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number? \n"))

        required_function = operations[operation_symbol]
        # print(f"The required_function is {required_function.__name__}")
        answer = required_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: \n")
        if response == 'y':
            num1 = answer
        if response == 'n':
            should_continue = False
            calculator()

calculator()


# operations[operation_symbol] gives the method value itself without calling it
# to call the method, pass in the params
# The Complete JavaScript Course 2021: From Zero to Expert!
# Section 10, 130. Higher order and callback