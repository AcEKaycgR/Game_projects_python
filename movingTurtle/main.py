from turtle import Turtle,Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.backward(10)


def turn_left():
    turt.left(5)


def turn_right():
    turt.right(5)


def pen_up():
    turt.penup()


def pen_down():
    turt.pendown()


def reset():
    screen.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkey(fun=pen_up, key="q")
screen.onkey(fun=pen_down, key="e")
screen.onkeypress(fun=reset, key="c")
screen.exitonclick()
