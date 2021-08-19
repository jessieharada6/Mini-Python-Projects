from tkinter import *
import pandas
from random import choice, randint, shuffle

BACKGROUND_COLOR = "#B1DDC6"
timer = None
front = True

#  ---------------------------- READ DATA ------------------------------- #
to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# words_dict = {row.French: row.English for index, row in data.iterrows()}
# print(words_dict)
# print(to_learn)
#  ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    # french
    global current_card, flip_timer
    # cancel timer for the next card
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    # print(current_card['French'])
    canvas.itemconfig(canvas_img, image=front_card_img)
    canvas.itemconfig(card_title, text=f"French",  fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    # flip after 3 seconds
    flip_timer = window.after(3000, flip_card)

#  ---------------------------- FLIP CARDS ---------------------------- #
def flip_card():
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(card_title, text=f"English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")

#  ---------------------------- SAVE WORDS ---------------------------- #
def is_known():
    global current_card
    to_learn.remove(current_card)
    # dict -> dataframe
    to_learn_df = pandas.DataFrame(to_learn)
    # dataframe -> csv
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
# must create outside of the function
# otherwise at the end of the function, reference will be lost
back_card_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_card_img)

# labels
# positions are based on the canvas position
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_img=PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness = 0, bd = 0, command=next_card)
unknown_button.grid(row=1, column=0)
correct_img=PhotoImage(file="images/right.png")
known_button = Button(image=correct_img, highlightthickness = 0, bd = 0, command=is_known)
known_button.grid(row=1, column=1)

# card_title and word display as desired
next_card()

window.mainloop()