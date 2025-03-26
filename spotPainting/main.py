from turtle import Turtle, Screen
import random
from typing import List

import colorgram

# color_list = []
# colors = colorgram.extract('spots2.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_list.append(new_color)
# print(color_list)


turt = Turtle()
screen = Screen()
screen.colormode(255)


color_list = [(165, 52, 81), (218, 154, 100), (43, 96, 148), (119, 162, 197), (57, 124, 61), (166, 25, 46), (204, 78, 102), (130, 190, 162), (25, 56, 131), (158, 83, 50), (211, 157, 27), (218, 84, 58), (229, 200, 94), (200, 138, 165), (53, 165, 110), (22, 47, 87), (56, 38, 45), (29, 90, 43), (214, 178, 201), (20, 71, 39), (171, 191, 220), (159, 204, 216), (235, 201, 3), (165, 207, 188), (112, 120, 162), (154, 32, 29)]
number_of_dots = 100
square_width = 10


def random_color():
    color = random.choice(color_list)
    return color


turt.penup()
turt.hideturtle()
turt.speed("fastest")
turt.setheading(225)
turt.forward(300)
turt.setheading(0)


for square_height in range(1, number_of_dots+1):
    turt.dot(20,random_color())
    turt.forward(50)

    if square_height % square_width == 0:
        turt.left(90)
        turt.forward(50)
        turt.left(90)
        turt.forward(500)
        turt.setheading(0)

screen.exitonclick()