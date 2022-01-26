from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)


my_screen = Screen()
my_screen.bgcolor("lightgreen")
my_screen.title("Hello World")
my_screen.setup(width=800, height=600)
my_screen.exitonclick()
