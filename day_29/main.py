from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import password_generator


def new_password():
    password = password_generator()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if email == "" or website == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(
            "Saved", f"Your password for {website} is {password}")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{email} | {website} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20, bg="#ffffff")


canvas = Canvas(window, width=200, height=200,
                highlightthickness=0, bg="#ffffff")
image = PhotoImage(file="logo.png")
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.grid(row=0, column=1)


website_label = Label(window, text="Website", bg="#ffffff")
website_label.grid(row=1, column=0)

website_entry = Entry(window, bg="#ffffff", width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(window, text="email/username", bg="#ffffff")
email_label.grid(row=2, column=0)

email_entry = Entry(window, bg="#ffffff", width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sirdiggaz@gmail.com")

password = Label(window, text="password", bg="#ffffff")
password.grid(row=3, column=0)

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1)
# password_entry.insert(0, password_generator())

generate_button = Button(
    window, text="Generate Password", command=new_password)
generate_button.grid(row=3, column=2)

add_button = Button(window, text="Add", width=36,
                    bg="#ffffff", command=save_password)
add_button.grid(row=4, column=1, sticky=W, columnspan=2)

window.mainloop()
