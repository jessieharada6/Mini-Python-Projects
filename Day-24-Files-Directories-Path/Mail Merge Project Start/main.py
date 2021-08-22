#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# my solution
# with open("Input/Names/invited_names.txt", mode="a") as file:
#     file.write("\n")
#
# with open("Input/Names/invited_names.txt") as file:
#     name_list = file.readlines()
#
# with open("Input/Letters/starting_letter.txt") as file:
#     letters = file.readlines()
#
# for name in name_list[:-1]:
#     with open(f"Output/ReadyToSend/letter_for_{name}", mode="a") as file:
#         new_title = letters[0].replace("[name]", name.strip())
#         file.write(new_title)
#         body = ""
#         for ele in letters[1:]:
#             body += ele
#         file.write(body)

# after looking at the solution
NAME = "[name]"
with open("Input/Names/invited_names.txt") as file:
    # return list
    name_list = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    # return string
    letter = file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace(NAME, stripped_name)
        # use "w", if doesn't exist, it creates, and always rewrite it
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as invites:
            invites.write(new_letter)
