from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed = 0.05
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2

    # move ball

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        self.collision_wall()

    # check for wall collision
    def collision_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

    # check for paddle collision
    def collision_paddle(self, paddle):
        if self.xcor() > paddle.xcor() - 40 and self.xcor() < paddle.xcor() + 40:
            if self.ycor() < paddle.ycor() + 50 and self.ycor() > paddle.ycor() - 50:
                self.dx *= -1
        self.ball_speed *= 0.9
