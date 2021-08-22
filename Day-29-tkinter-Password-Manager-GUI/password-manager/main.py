from tkinter import *
# it is not a class or constants, it is a module of code
# * = class and constants
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# BLACK = "#171717"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list =  [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join( [char for char in password_list])
    pwd_entry.insert(0, string=password)
    #  copy to clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_value = web_entry.get()
    info_value = info_entry.get()
    pwd_value = pwd_entry.get()

    if len(web_value) == 0 or len(pwd_value) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_value,
                                       message=f"These are the messages entered: \n Email: {info_value}"
                                               f"\n Password: {pwd_value} \n Is it ok to save?")
        if is_ok:
            with open("pwd_file.txt", mode="a") as file:
                file.write(f"{web_value} | {info_value} | {pwd_value}\n")

        # [index1, index2]
        # web_entry.delete(0, 'end') - also works
        web_entry.delete(0, END)
        pwd_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#highlightbackground=BLACK for boarder color
canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# labels
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)
info_label = Label(text="Email/Username: ")
info_label.grid(column=0, row=2)
pwd_label = Label(text="Password: ")
pwd_label.grid(column=0, row=3)

# entries
web_entry = Entry(width=35)
# cursor starting here
web_entry.focus()
# columnspan spans across the columns, and sticky aligns entries
web_entry.grid(column=1, row=1, columnspan= 2, sticky="ew")

info_entry = Entry(width=35)
# pre-populate value at the email
info_entry.insert(0, string="harada@gmail.com")
info_entry.grid(column=1, row=2, columnspan= 2, sticky="ew")

pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row=3, columnspan= 1,  sticky="ew")

# buttons
pwd_button = Button(text="Generate Password", command=generate_password)
pwd_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()