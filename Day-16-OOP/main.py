# Python Packages 
# package is a bunch of modules
# How to Add Python Packages and use PyPi
# pypi.org
# pycharm - preference - go to project - python interpretor

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"​What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) == True:
            if money_machine.make_payment(coffee.cost) == True:
                coffee_maker.make_coffee(coffee)