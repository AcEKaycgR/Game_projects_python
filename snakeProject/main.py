import time
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=snake.snake_up,key="Up")
screen.onkey(fun=snake.snake_down,key="Down")
screen.onkey(fun=snake.snake_left,key="Left")
screen.onkey(fun=snake.snake_right,key="Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:         #this is a method called slicing list[num1:num2]
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
