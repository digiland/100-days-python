from textwrap import fill
from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(self.window, text="Score: 0/0",
                           bg=THEME_COLOR, fg="white", font="Arial 10 bold")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=290, text="Quiz",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image,
                              bg=THEME_COLOR, command=self.true_pressed)
        self.correct.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=false_image,
                            bg=THEME_COLOR, command=self.false_pressed)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Fin")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
