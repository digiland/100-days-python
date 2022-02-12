import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")
cars.move_cars()

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # detect coliision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.increase_speed()
        score.increase_level()

screen.exitonclick()
