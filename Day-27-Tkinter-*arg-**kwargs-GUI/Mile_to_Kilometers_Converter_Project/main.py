from tkinter import *

def button_click():
    miles=float(miles_input.get())
    km_value = round(1.609 * miles)
    # km_value_label.config(text=km_value")
    km_value_label.config(text=f"{km_value}")

window = Tk()
window.title("Mile to Kilometer Convertor")
window.minsize(width=250,height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label=Label(text="is equal to")
is_equal_to_label.grid(column=0,row=1)

km_value_label=Label(text="0")
km_value_label.grid(column=1,row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate", command=button_click)
calculate_button.grid(column=1,row=2)

window.mainloop()