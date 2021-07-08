from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if (guess < answer):
        print("Too Low.")
        return turns - 1
    elif (guess > answer):
        print("Too High.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL

def game():
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # in solution, they tell the answer straightaway
    answer = randint(1, 100) 
    print(f"Pssst, the correct answer is {answer}") 

    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
            
game()