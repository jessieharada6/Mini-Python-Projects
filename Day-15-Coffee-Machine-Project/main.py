from resource import resources, MENU

resources['money'] = 0
def print_report(resources):
    money = ""
    if 'money' in resources:
        money = f"\nMoney: ${resources['money']}"
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml{money}")


# def check_resources(menu, resources, input): 
#     if input in menu:
#         if resources["water"] < menu[input]["ingredients"]["water"]: 
#             print(f"Sorry. There is not enought water")
#             return False
#         if input != "espresso" and resources["milk"] < menu[input]["ingredients"]["milk"]:
#             print(f"Sorry. There is not enought milk")
#             return False
#         if resources["coffee"] < menu[input]["ingredients"]["coffee"]:
#             print(f"Sorry. There is not enought coffee")
#             return False
#     return True
    
# print(MENU["latte"]["ingredients"]["milk"])
# check_resources(MENU, resources, "latte")

def check_resources(menu, resources, input): 
    for item in menu[input]["ingredients"]:
        if menu[input]["ingredients"][item] > resources[item]:
            print(f"Sorry. There is not enought {item}")
            return False
    return True

# for item in MENU["latte"]["ingredients"]:
#     print(MENU["latte"]["ingredients"][item])

def process_coins():
    print(f"Please insert coins.")
    quarters = int(input(f"how many quarters?: "))
    dimes = int(input(f"how many dimes?: "))
    nickles = int(input(f"how many nickles?: "))
    pennies = int(input(f"how many pennies?: "))
    amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return amount

# print(process_coins(1, 2, 1, 2))

def check_transaction(menu, resources, input):
    amount = process_coins()
    price = 0
    if input in menu:
        price = menu[input]['cost']
    
    if price > amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif price < amount:
        change = round(amount - price, 2)
        print(f"Here is ${change} in change.")
        resources['money'] += price
        return True
    else:
        return True


# check_transaction(MENU, resources, "latte", 10, 10, 10, 10)
# print(resources)

def make_coffee(menu, resources, input):
    if check_resources(menu, resources, input) and check_transaction(menu, resources, input):
        if input in menu:
            resources['water'] -= menu[input]['ingredients']['water']
            resources['coffee'] -= menu[input]['ingredients']['coffee']
            if input != "espresso":
                resources['milk'] -= menu[input]['ingredients']['milk']
            print(f"Here is your {input} ☕️. Enjoy!")
    return resources

# print(resources)
# print(make_coffee(MENU, resources, "latte", 10, 10, 10, 10))
# print(resources)

def order_coffee():
    is_order_over = False
    while not is_order_over:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "espresso" or order == "latte" or order == "cappuccino":
            # menu_order = MENU[order]
            if check_resources(MENU, resources, order) == True:
                make_coffee(MENU, resources, order)
        if order == "report":
            print_report(resources)
        if order == "off":
            is_order_over = True


order_coffee()