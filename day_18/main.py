from turtle import Turtle, Screen, pencolor
import random

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.color("red")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]


def draw_shape(turtle, size, angle, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(angle)


for i in range(3, 11):
    timmy.pencolor(random.choice(colors))
    draw_shape(timmy, 100, 360/i, i)


def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_circle(turtle, size):
    for i in range(360):
        turtle.forward(size)
        turtle.left(1)


draw_circle(timmy, 2)
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
draw_square(timmy, 20)


def dashed_line(turtle, size):
    for i in range(20):
        turtle.forward(size)
        turtle.penup()
        turtle.forward(size)
        turtle.pendown()


dashed_line(timmy, 20)


screen.exitonclick()
