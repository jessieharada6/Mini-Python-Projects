#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

def compare(user_num, real_num):
    if (user_num > real_num):
        return "Too high."
    elif (user_num < real_num):
        return "Too low."

def get_number():
    return random.randint(1, 100)

def guess_number():
    count = 0
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {get_number()}")
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if level =='hard':
        count = 5
    elif level == 'easy':
        count = 10
    real_num = get_number()

    while count > 0:
        print(f"You have {count} attempts remaining to guess the number. {real_num}")
        user_num = int(input(f"Make a guess: "))
        if real_num != user_num:
            print(f"{compare(user_num, real_num)}")
            count -= 1
            print(f"Guess again.")
        else:
            print(f"You got it! The answer was {real_num}.")
            break
    
    if count == 0:
        print(f"You've run out of guesses, you lose.")

guess_number()
    


    


