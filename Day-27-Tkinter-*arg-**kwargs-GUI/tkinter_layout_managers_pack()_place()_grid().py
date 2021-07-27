from tkinter import *

def button_clicked():
    text = input.get()
    if text != "":
        my_label.config(text=text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add paddings among widgets
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# add paddings for one widget
my_label.config(padx=50, pady=50)

# Button
another_button = Button(text="New Button")
# button.pack()
# x: 2, y:0
another_button.grid(column=2, row=0)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# keep window on screen
# must be at the end of the program
window.mainloop()


# tkinter layout manager:
# any widgets/components must use one of the following three in order for the item to show on screen
# Pack:
# by default, position each component as top down
# can specify side

# Place:
# precise positioning
# component.place(x=0, y=0)

# Grid: preferred
# rows: horizontal, columns: vertical
# relative to other items, if there are no other grid, even specified as column=5, it will still place as 0

# can't mix up grid and pack in the same program
# error: slaves managed by grid