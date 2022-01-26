import random
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


jerry = Turtle()


jerry.speed("fastest")


def spirograph(gap):
    for i in range(int(360/gap)):
        jerry.pencolor(random_color())
        jerry.circle(100)
        current_heading = jerry.heading()
        jerry.setheading(current_heading + gap)


spirograph(5)


screen.exitonclick()
