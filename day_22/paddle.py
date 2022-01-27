from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def paddle_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
