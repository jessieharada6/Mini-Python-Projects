# blind-auction

from replit import clear
from art import logo

print(logo)
bid = {}

def find_highest_bidder(bid):
    max = 0
    name = ""
    for key in bid:
        price = bid[key]
        if max < price:
            max = price
            name = key
    print(f"The winner is {name} with a bid of ${max}")

bid_end = False
while not bid_end:
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n"))
    bid[name] = price
    restart = input("Are there any other bidders? Type 'yes' or 'no' \n")
    if (restart == "yes"):
        clear()
    elif (restart == "no"):
        clear()
        find_highest_bidder(bid)
        bid_end = True
# print(bid)

