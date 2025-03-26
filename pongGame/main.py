from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down, "Down")
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move_ball()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.xcor() > 330 and ball.distance(rpaddle) < 50 or ball.xcor() < -330 and ball.distance(lpaddle) < 50:
        ball.x_bounce()

    if ball.xcor() > 375:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        time.sleep(0.2)
        ball.reset_position()

    if ball.xcor() < -384:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        time.sleep(0.2)
        ball.reset_position()
screen.exitonclick()
