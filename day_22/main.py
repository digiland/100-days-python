from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
score = ScoreBoard()
ball = Ball()

# paddle A
paddle_a = Paddle(-350, 0)


# paddle B
paddle_b = Paddle(350, 0)


screen.listen()
screen.onkeypress(paddle_a.paddle_up, "w")
screen.onkeypress(paddle_a.paddle_down, "s")

screen.onkeypress(paddle_b.paddle_up, "Up")
screen.onkeypress(paddle_b.paddle_down, "Down")

game_over = False

while not game_over:
    ball.move()
    screen.update()
    ball.collision_paddle(paddle_a)
    ball.collision_paddle(paddle_b)
    time.sleep(ball.ball_speed)

    score_a, score_b = 0, 0

    # detect miss
    if ball.xcor() > 390:
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.dx *= -1
        score.update_score_a()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.dx *= -1
        score.update_score_b()


screen.exitonclick()
