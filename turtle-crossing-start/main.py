import time
from turtle import Screen
from player import Player
# from car_manager import CarManager
from car_manager_trial import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()
    for cars in car_manager.All_CAR:
        for car in cars:
            if player.distance(car) < 15:
                game_is_on = False
                scoreboard.game_over()

    if player.is_at_finish_line():
        player.reset()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()

