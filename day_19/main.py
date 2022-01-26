from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fowards():
    tim.forward(100)


def move_backwards():
    tim.backward(100)


def clockwise():
    h = tim.heading() - 5
    tim.setheading(h)


def anti_clockwise():
    h = tim.heading() + 5
    tim.setheading(h)


screen.listen()
screen.onkey(move_fowards, "d")
screen.onkey(move_backwards, "a")
screen.onkey(clockwise, "w")
screen.onkey(anti_clockwise, "s")
screen.onkey(tim.clear, "c")
screen.exitonclick()
