from turtle import Turtle, Screen, forward
import random

screen = Screen()
screen.colormode(255)


hirst = Turtle()

colors = [(62, 185, 237), (4, 188, 242), (49, 107, 182), (141, 64, 120), (98, 229, 252),
          (98, 112, 188), (139, 18, 64), (150, 230, 253), (184, 89, 143), (234, 59, 7)]

hirst.penup()
hirst.hideturtle()
hirst.goto(25-screen.window_width() / 2, screen.window_height() / 2 - 25)

draw = True

while draw:
    hirst.dot(40, random.choice(colors))
    hirst.forward(40*2)
    if hirst.xcor() > screen.window_width() / 2:
        print(hirst.ycor())
        hirst.goto(25-screen.window_width() / 2, hirst.ycor() - 70)

    if hirst.ycor() < -screen.window_height() / 2:
        draw = False
        print("Done")


screen.exitonclick()
