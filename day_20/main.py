from turtle import Turtle, Screen
import time
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import random


screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend_snake()
        # snake.add_segment()

    # detect collision with border
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        score.reset()
        snake.reset()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
