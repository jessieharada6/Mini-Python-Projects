rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
options = [rock, paper, scissors]
human_decision = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n")

human_choice = int(human_decision)
if human_choice > 2 or human_choice < 0:
  print("You typed an invalid number, please retry")
else: 
  print(f"human chose: \n {options[human_choice]}")
  computer_choice = random.randint(0, 2)
  print(f"computer chose: \n {options[computer_choice]}")

  if (human_choice == 0 and computer_choice == len(options) - 1) or (human_choice == len(options) - 1 and computer_choice == 1) or (human_choice == 1 and computer_choice == 0) :
    print("You won")
  elif human_choice == computer_choice:
    print("It's a draw")
  else:
    print("You lost")
