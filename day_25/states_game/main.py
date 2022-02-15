import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("States Game")

image = "states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct = 0

data = pd.read_csv("50_states.csv")

states = data.state.tolist()
while correct < 50:
    answer = screen.textinput(
        f"{correct}/50 States Correct", "Guess a state").capitalize()

    if answer in states:
        correct += 1
        states.remove(answer)
        state = data[data.state == answer]
        print(f"{state.x} {state.y}")

        # write text to screen
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(int(state.x), int(state.y))
        text.write(f"{answer}", font=("Arial", 12, "normal"))


screen.exitonclick()
