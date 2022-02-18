import time
from cProfile import label
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark["text"] = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown(work_sec)
        label.config(text="Work")
    elif reps == 8:
        countdown(long_break)
        label.config(text="Long Break", fg=PINK)
    else:
        countdown(short_break)
        label.config(text="Short Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps

    count_min = count // 60
    count_sec = count % 60
    count_sec = '0' + str(count_sec) if count_sec < 10 else count_sec

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
window.minsize(500, 500)


label = Label(text="Timer", font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN)
label.pack(side=TOP)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(0, 0, anchor=NW, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", font=(
    FONT_NAME, 35, "bold"), fill="white")
canvas.pack()
start_button = Button(text="Start", font=(FONT_NAME, 20),
                      bg=GREEN, command=start_timer)
start_button.pack(side=LEFT)
reset_button = Button(text="Reset", font=(
    FONT_NAME, 20), bg=RED, command=reset_timer)
reset_button.pack(side=RIGHT)

check_mark = Label(text="", font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN)
check_mark.pack(side=BOTTOM)

window.mainloop()
