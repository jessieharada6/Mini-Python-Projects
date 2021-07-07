# Higher Lower Game 
import random
from game_data import data
from art import vs
from art import logo


# from replit import clear

def get_data():
    """Get random data, make sure they are not the same"""
    data_a = ""
    data_b = ""
    while data_a == data_b:
        data_a = random.choice(data)
        data_b = random.choice(data)
    return data_a, data_b


def compare(data_a, data_b):
    """Compare the result"""
    if data_a['follower_count'] < data_b['follower_count']:
        return 'B'
    else:
        return 'A'


def format_data(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}"


def play_game():
    print(logo)
    current_score = 0
    is_game_over = False
    while not is_game_over:
        data_set = get_data()
        data_a = data_set[0]
        data_b = data_set[1]
        print(f"Compare A: {format_data(data_a)}")
        print(vs)
        print(f"Against B: {format_data(data_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        # clear()
        # print(logo)
        if guess == compare(data_a, data_b):
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            is_game_over = True


play_game()
