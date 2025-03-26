from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_is_on = False
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
turtle_name = ["turtle_1", "turtle_2", "turtle_3", "turtle_4", "turtle_5", "turtle_6", ]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_coordinate = -70
all_turtles = []


steps = 10
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 30
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winner = str(turtle.pencolor())
            print(f"The winner is {winner} ")
            if user_bet == turtle.color():
                print("You have won")
            else:
                print("You have lost")
        else:
            steps = random.randint(1,10)
            turtle.forward(steps)


screen.exitonclick()
