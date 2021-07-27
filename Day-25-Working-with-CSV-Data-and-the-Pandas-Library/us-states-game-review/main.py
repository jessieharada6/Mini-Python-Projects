import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Verdana", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. State Game")

# add image to turtle object - turtle works with gif image
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# TODO: data.state.to_list() also works
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name")
    title_answer = answer_state.title()
    # correct answer
    if title_answer in all_states:
        if title_answer not in guessed_states:
            guessed_states.append(title_answer)
        # TODO: to create another object, module.Class()
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        row = data[data.state == title_answer]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state, align=ALIGNMENT, font=FONT)
    if title_answer == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # use list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")