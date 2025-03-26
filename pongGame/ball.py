from turtle import Turtle

X_COR = 5
Y_COR = 5
SPEED = 0.04


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = X_COR
        self.y_move = Y_COR
        self.move_speed = SPEED
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        # self.setheading(45)
        self.color("white")
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1
        # new_heading = self.heading() - 90
        # self.setheading(new_heading)

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.97

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = SPEED
        self.x_bounce()

