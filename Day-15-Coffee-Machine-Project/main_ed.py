from resource import resources, MENU

resources['money'] = 0
def print_report(resources):
    """print the report"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${resources['money']}")

# MENU["latte"]["ingredients"]
def check_resources(ingredients, resources): 
    """check if the resources are sufficient based on what the customer orders and the current report"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# for item in MENU["latte"]["ingredients"]:
#     print(MENU["latte"]["ingredients"][item]) 
#     50, 18 

def process_coins():
    """calculate the amount received from the customer"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    return amount

def is_transaction_successful(money_received, drink_cost):
    """check if the money received from the customer is sufficient, add to the current money in the report"""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change != 0:
            print(f"Here is ${change} in change.")
        resources['money'] += drink_cost
        return True

def make_coffee(ingredients, resources, order):
    """Deduct the required ingredients from the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")

# for item in MENU["latte"]["ingredients"]:
#     print(MENU["latte"]["ingredients"][item])

def order_menu():
    is_on = True
    while is_on:
        choice = input("​What would you like? (espresso/latte/cappuccino): ")
        if choice == "report":
            print_report(resources)
        elif choice == "off":
            is_on = False
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            order = MENU[choice]
            if check_resources(order["ingredients"], resources) == True:
                payment = process_coins()
                if is_transaction_successful(payment, order["cost"]) == True:
                    make_coffee(order["ingredients"], resources, choice)

order_menu()