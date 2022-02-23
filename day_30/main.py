import random
from time import sleep
from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

# load file
italian = "data/italian.csv"
french = "data/french_words.csv"


def load_file(filename):
    """Loads a file and returns the contents."""
    data = pd.read_csv(filename)
    to_learn = data.to_dict(orient="records")
    return to_learn


print("Welcome to Flashy please choose a language")
language_choice = input("Please choose a language: ")
to_learn = f"data/{language_choice}_to_learn.csv"
if language_choice == "Italian":
    try:
        cards = load_file(to_learn)
    except FileNotFoundError:
        cards = load_file(italian)
elif language_choice == "French":
    try:
        cards = load_file(to_learn)
    except FileNotFoundError:
        cards = load_file(french)


def flip_card(card):
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text=language_choice, fill="black")
    canvas.itemconfig(
        card_word, text=current_card[language_choice], fill="black")
    flip_timer = window.after(3000, flip_card, current_card)


def is_known():
    cards.remove(current_card)
    print(len(cards))
    data = pd.DataFrame(cards)
    data.to_csv(f"data/{language_choice}_to_learn.csv")

    next_card()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(window, width=800, height=528,
                highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(0, 0, anchor=NW, image=card_front)

card_title = canvas.create_text(
    400, 150, text="Language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 300, text="Word", font=("Helvetica", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(window, image=wrong_image,
               highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

correct_image = PhotoImage(file="images/right.png")
correct = Button(window, image=correct_image,
                 highlightthickness=0, command=is_known)
correct.grid(row=1, column=1)

next_card()

window.mainloop()
