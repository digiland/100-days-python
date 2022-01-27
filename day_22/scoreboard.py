from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_a = 0
        self.score_b = 0
        self.penup()
        self.goto(0, 240)
        self.color("white")
        self.hideturtle()
        self.write(f" {self.score_a} vs {self.score_b}", align="center",
                   font=("Courier", 50, "normal"))

    def update_score_a(self):
        self.score_a += 1
        self.clear()
        self.write(f" {self.score_a} vs {self.score_b}", align="center",
                   font=("Courier", 50, "normal"))

    def update_score_b(self):
        self.score_b += 1
        self.clear()
        self.write(f" {self.score_a} vs {self.score_b}", align="center",
                   font=("Courier", 50, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center",
                   font=("Courier", 24, "normal"))
