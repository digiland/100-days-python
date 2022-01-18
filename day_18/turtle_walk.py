import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

colors = ["medium slate blue", "spring green", "pink", "gold", "CornflowerBlue",
          "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


tom = Turtle()
tom.pensize(10)
tom.speed("fastest")
directions = [0, 90, 180, 270]
for i in range(100):
    tom.pencolor(random_color())
    tom.forward(30)
    tom.setheading(random.choice(directions))


screen.exitonclick()
