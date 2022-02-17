from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


miles = Entry(width=10)
miles.grid(column=0, row=0)

km = Label(text=f"Kilometers:")
km.grid(column=1, row=0)


def convert():
    km.config(text=f"Kilometers: {int(miles.get() )* 1.60934}")


button = Button(text="Convert", command=convert)
button.grid(column=2, row=0)


window.mainloop()
