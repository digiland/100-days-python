import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
bet = screen.textinput("Choose color", "Make your bet: ")
all_turtles = []

y = -100

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-240, y+40)
    all_turtles.append(tim)
    y += 40


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        dist = random.randint(0, 10)
        turtle.forward(dist)
        if turtle.xcor() > 230:
            is_race_on = False
            if bet == turtle.pencolor():
                print("You win")
            else:
                print(turtle.pencolor())


screen.exitonclick()
