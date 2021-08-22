import turtle
import pandas
from states import States

ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")

screen = turtle.Screen()
screen.title("U.S. State Game")

# add image to turtle object
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
states_guess = States()

is_game_on = True
# pop up window
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name")
scores = 0
while is_game_on:
    title_answer = answer_state.title()
    # correct answer
    if title_answer.title() in states:
        row = data[data.state == title_answer]
        states_guess.add_states(int(row.x), int(row.y), title_answer)
        scores = states_guess.increase_score(title_answer)
    answer_state = screen.textinput(title=f"{scores}/50 States Correct",
                                        prompt="What's another state's name")

# print the coordinates upon mouse click
# this is how to find the coordinates on the .gif
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
# keep screen open
turtle.mainloop()

