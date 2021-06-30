# Review on For & While loop, if/else, lists, strings, range, modules etc.


from replit import clear
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
lives = 6
#random words
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
print(chosen_word)
display = []
# for c in chosen_word:
#     display.append("_")
for _ in range(word_len):
    display += "_"

#user guess
end_of_game = False
already_guessed = []
# while True: 
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    # clear screen
    clear()
    # the letter has been guessed before
    if guess in display:
        print(f"You have guessed this letter {guess} before")
    # guessed a correct letter
    for pos in range(word_len):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(f"{''.join(display)}")
    # guessed a wrong letter
    if guess not in chosen_word:
        print(f"The letter {guess} that you guessed is not in the word")
        lives -= 1
        # lose the game
        if lives == 0:
            print("You lose.")
            break;
    print(hangman_art.stages[lives])
    # win the game
    if "_" not in display:
        end_of_game = True
        print("You win")