# import tkinter
from tkinter import *
# now we no longer need to do tkinter.Tk(), or tkinter.Button()

# init screen
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# components inside the window
# e.g. Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# place in the screen - showing label - always need to call
# **kw - kw can be anything, mandatory is **
my_label.pack()
# TO SET/UPDATE
my_label["text"] = "new text"
my_label.config(text="new text")

# e.g. Entry: input
input = Entry(width=10)
input.pack()

# e.g. Button
def button_clicked():
    # my_label["text"] = "I got clicked"
    # my_label.config(text="I got clicked")
    # input.get() returns the input as a string
    text = input.get()
    if text != "":
        my_label.config(text=text)

button = Button(text="Click Me", command=button_clicked)
button.pack()




# keep window on screen
# must be at the end of the program
window.mainloop()